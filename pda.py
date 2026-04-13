import logging

class RunningConfig:
    def __init__(self, input_str, stack_symbol, initial_state):
        self.stack = stack_symbol
        self.state = initial_state
        self.remaining_input = input_str

    def printState(self):
        print("")
        print(f"Current state: {self.state}")
        print(f"Remaining input: {self.remaining_input}")
        print(f"Current stack: {self.stack}")
        print("")

    def to_dict(self):
        return {
            "state": self.state,
            "remaining_input": self.remaining_input,
            "stack": self.stack.copy()
        }

class PDA:
    def __init__(self, states, input_symbols, stack_symbols,
                 transitions, initial_state,
                 initial_stack_symbol, final_states):
        self.states = states
        self.input_symbols = input_symbols
        self.stack_symbols = stack_symbols
        self.transitions = transitions
        self.initial_state = initial_state
        self.initial_stack_symbol = initial_stack_symbol
        self.final_states = final_states
        self.validate()

    def validate(self):
        if self.initial_state not in self.states:
            logging.error(f"Initial state {self.initial_state} is invalid!")

        for f in self.final_states:
            if f not in self.states:
                logging.error(f"Final state {f} is invalid!")

        if self.initial_stack_symbol not in self.stack_symbols:
            logging.error(f"Invalid initial stack symbol")

    def exec_web(self, input_str):
        trace = []
        current_config = []

        initial_cfg = RunningConfig(input_str, [self.initial_stack_symbol], self.initial_state)
        current_config.append(initial_cfg)

        trace.append({
            "message": "Step 1",
            "configs": [initial_cfg.to_dict()]
        })

        step_counter = 2

        while current_config != []:
            new_config = []
            step_trace = {
                "message": f"Step {step_counter}",
                "configs": []
            }

            for idx, c in enumerate(current_config):
                
                if self.accepted(c):
                    trace.append({"status": "Accepted", "configs": [c.to_dict()]})
                    return trace

                new = 0

                if c.remaining_input:
                    new = self.update_configs(c)
                elif (c.state in self.transitions and
                      '' in self.transitions[c.state] and
                      c.stack[-1] in self.transitions[c.state]['']):
                    new = self.update_configs(c)

                if new:
                    new_config += new
                    for n in new:
                        step_trace["configs"].append(n.to_dict())
                        
                        if self.accepted(n):
                            trace.append(step_trace)
                            trace.append({"status": "Accepted", "configs": [n.to_dict()]})
                            return trace
                else:
                    step_trace["configs"].append({
                        "state": c.state,
                        "remaining_input": c.remaining_input,
                        "stack": c.stack.copy(),
                        "info": "Dead State reached!"
                    })

            if len(step_trace["configs"]) > 0:
                trace.append(step_trace)

            current_config = new_config
            step_counter += 1

        trace.append({"status": "Rejected", "configs": []})
        return trace

    def exec(self, input_str):
        current_config = []

        current_config.append(RunningConfig(
            input_str, [self.initial_stack_symbol], self.initial_state
        ))

        print("\x1b[32mInitial configuration: \x1b[0m")
        current_config[0].printState()

        while current_config != []:
            new_config = []

            for idx, c in enumerate(current_config):
                new = 0

                if self.accepted(c):
                    print("\x1b[35mAccepted!\x1b[0m")
                    return

                print(f"\x1b[32mRunning for configuration {idx + 1}:\n\x1b[0m")

                if c.remaining_input:
                    new = self.update_configs(c)
                elif (c.state in self.transitions and
                      '' in self.transitions[c.state] and
                      c.stack[-1] in self.transitions[c.state]['']):
                    new = self.update_configs(c)

                if new:
                    new_config += new
                    for i, n in enumerate(new):
                        print(f"\x1b[34mOutput configuration {i + 1}:\x1b[0m")
                        n.printState()
                else:
                    print("\x1b[31mDead State reached!\x1b[31m")

            current_config = new_config

        print("\x1b[31mRejected!\x1b[0m")
        return

    def accepted(self, config):
        if config.remaining_input:
            return False

        if config.state in self.final_states and config.stack == [self.initial_stack_symbol]:
            return True

        return False

    def update_configs(self, config):
        transitions = []

        if config.remaining_input:
            transitions = self.get_transitions(config.state, config.remaining_input[0], config.stack[-1])

        if not transitions:
            transitions = self.get_transitions(config.state, "", config.stack[-1])

        new_configs = []

        for transition in transitions:
            input_symbol = transition[0]
            new_state = transition[1]
            new_stack_top = transition[2]
            remaining_input = config.remaining_input

            if input_symbol:
                remaining_input = remaining_input[1:]

            new_configs.append(
                RunningConfig(remaining_input, 
                    self.stack_replace_top(config.stack.copy(), new_stack_top),
                    new_state
                )
            )

        return new_configs

    def get_transitions(self, state, symbol, stack_symbol):
        out = []
        if state in self.transitions and symbol in self.transitions[state] and stack_symbol in self.transitions[state][symbol]:
            for transition in self.transitions[state][symbol][stack_symbol]:
                out.append([symbol, transition[0], transition[1]])
        return out

    def stack_replace_top(self, stack, stack_top):
        if stack_top == "":
            stack.pop()
        else:
            stack.pop()
            for j in range(len(stack_top) - 1, -1, -1):
                stack.append(stack_top[j])

        return stack