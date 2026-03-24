from pda import PDA


class Languages:
    languages = {
        "aNbN":
        # L = {aNbN : N >= 0}
        PDA(
            states=['q0', 'q1'],
            input_symbols=['a', 'b'],
            stack_symbols=['A', 'Z'],
            transitions={
                'q0': {
                    '': {
                        'Z': [
                            ['q1', 'Z']
                        ],
                    },
                    'a': {
                        'Z': [
                            ['q0', ['A', 'Z']]
                        ],
                        'A': [
                            ['q0', ['A', 'A']]
                        ]
                    },
                    'b': {
                        'A': [
                            ['q1', '']
                        ]
                    },
                },
                'q1': {
                    'b': {
                        'A': [
                            ['q1', '']
                        ]
                    },
                },
            },
            initial_state='q0',
            initial_stack_symbol='Z',
            final_states=['q1']
        ),

        "aNb2N":
        # L = {aNb2N : N >= 0}
        PDA(
            states=['q0', 'q1', 'q2'],
            input_symbols=['a', 'b'],
            stack_symbols=['A', 'Z'],
            transitions={
                'q0': {
                    '': {
                        'Z': [
                            ['q2', 'Z']
                        ],
                    },
                    'a': {
                        'Z': [
                            ['q0', ['A', 'A', 'Z']]
                        ],
                        'A': [
                            ['q0', ['A', 'A', 'A']]
                        ]
                    },
                    'b': {
                        'A': [
                            ['q1', '']
                        ]
                    },
                },
                'q1': {
                    'b': {
                        'A': [
                            ['q1', '']
                        ]
                    },
                    '': {
                        'Z': [
                            ['q2', 'Z']
                        ],
                    },
                },
            },
            initial_state='q0',
            initial_stack_symbol='Z',
            final_states=['q2']
        ),

        "aMbNcM+N":
        # L = {aMbNc(M+N) : M,N >= 0}
        PDA(
            states=['q0', 'q1', 'q2', 'q3'],
            input_symbols=['a', 'b', 'c'],
            stack_symbols=['A', 'Z'],
            transitions={
                'q0': {
                    '': {
                        'Z': [
                            ['q3', 'Z']
                        ],
                    },
                    'a': {
                        'Z': [
                            ['q0', ['A', 'Z']]
                        ],
                        'A': [
                            ['q0', ['A', 'A']]
                        ]
                    },
                    'b': {
                        'Z': [
                            ['q1', ['A', 'Z']]
                        ],
                        'A': [
                            ['q1', ['A', 'A']]
                        ]
                    },
                    'c': {
                        'A': [
                            ['q2', '']
                        ],
                    },
                },
                'q1': {
                    'b': {
                        'A': [
                            ['q1', ['A', 'A']]
                        ]
                    },
                    'c': {
                        'A': [
                            ['q2', '']
                        ]
                    },
                },
                'q2': {
                    '': {
                        'Z': [
                            ['q3', 'Z']
                        ]
                    },
                    'c': {
                        'A': [
                            ['q2', '']
                        ]
                    },
                },
            },
            initial_state='q0',
            initial_stack_symbol='Z',
            final_states=['q2']
        ),

        "aNbMcMdN":
        # L = {aNbMcMdN : M,N >= 0}
        PDA(
            states=['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6'],
            input_symbols=['a', 'b', 'c', 'd'],
            stack_symbols=['A', 'B', 'Z'],
            transitions={
                'q0': {
                    '': {
                        'Z': [
                            ['q4', 'Z']
                        ],
                    },
                    'a': {
                        'Z': [
                            ['q0', ['A', 'Z']]
                        ],
                        'A': [
                            ['q0', ['A', 'A']]
                        ],
                    },
                    'b': {
                        'Z': [
                            ['q5', ['B', 'Z']]
                        ],
                        'A': [
                            ['q1', ['B', 'A']]
                        ],
                    },
                    'd': {
                        'A': [
                            ['q3', '']
                        ],
                    },
                },
                'q1': {
                    'b': {
                        'B': [
                            ['q1', ['B', 'B']]
                        ],
                    },
                    'c': {
                        'B': [
                            ['q2', '']
                        ],
                    },
                },
                'q2': {
                    'c': {
                        'B': [
                            ['q2', '']
                        ],
                    },
                    'd': {
                        'A': [
                            ['q3', '']
                        ]
                    },
                },
                'q3': {
                    '': {
                        'Z': [
                            ['q4', 'Z']
                        ],
                    },
                    'd': {
                        'A': [
                            ['q3', '']
                        ]
                    },
                },
                'q5': {
                    'b': {
                        'B': [
                            ['q5', ['B', 'B']]
                        ],
                    },
                    'c': {
                        'B': [
                            ['q6', '']
                        ]
                    },
                },
                'q6': {
                    '': {
                        'Z': [
                            ['q4', 'Z']
                        ],
                    },
                    'c': {
                        'B': [
                            ['q6', '']
                        ]
                    },
                },
            },
            initial_state='q0',
            initial_stack_symbol='Z',
            final_states=['q4']
        ),

        "wcwR":
        # L = {wcwR : w ∈ (a+b)*}
        PDA(
            states=['q0', 'q1', 'q2', 'q3'],
            input_symbols=['a', 'b'],
            stack_symbols=['A', 'B', 'Z'],
            transitions={
                'q0': {
                    'c': {
                        'Z': [
                            ['q3', 'Z']
                        ],
                    },
                    'a': {
                        'Z': [
                            ['q0', ['A', 'Z']]
                        ],
                        'A': [
                            ['q0', ['A', 'A']]
                        ],
                        'B': [
                            ['q0', ['A', 'B']]
                        ],
                    },
                    'b': {
                        'Z': [
                            ['q0', ['B', 'Z']]
                        ],
                        'A': [
                            ['q0', ['B', 'A']]
                        ],
                        'B': [
                            ['q0', ['B', 'B']]
                        ],
                    },
                    'c': {
                        'A': [
                            ['q1', 'A']
                        ],
                        'B': [
                            ['q1', 'B']
                        ],
                    },
                },
                'q1': {
                    '': {
                        'Z': [
                            ['q2', 'Z']
                        ],
                    },
                    'a': {
                        'A': [
                            ['q1', '']
                        ],
                    },
                    'b': {
                        'B': [
                            ['q1', '']
                        ],
                    },
                },
                'q3': {
                    '': {
                        'Z': [
                            ['q2', 'Z']
                        ],
                    },
                },
            },
            initial_state='q0',
            initial_stack_symbol='Z',
            final_states=['q2']
        ),

        "wwR":
        # L = {wwR : w ∈ (a+b)*}
        PDA(
            states=['q0', 'q1', 'q2'],
            input_symbols=['a', 'b'],
            stack_symbols=['A', 'B', 'Z'],
            transitions={
                'q0': {
                    '': {
                        'Z': [
                            ['q2', 'Z']
                        ],
                    },
                    'a': {
                        'Z': [
                            ['q0', ['A', 'Z']]
                        ],
                        'A': [
                            ['q0', ['A', 'A']],
                            ['q1', ''],
                        ],
                        'B': [
                            ['q0', ['A', 'B']]
                        ],
                    },
                    'b': {
                        'Z': [
                            ['q0', ['B', 'Z']]
                        ],
                        'A': [
                            ['q0', ['B', 'A']]
                        ],
                        'B': [
                            ['q0', ['B', 'B']],
                            ['q1', ''],
                        ],
                    },
                },
                'q1': {
                    '': {
                        'Z': [
                            ['q2', 'Z']
                        ]
                    },
                    'a': {
                        'A': [
                            ['q1', '']
                        ]
                    },
                    'b': {
                        'B': [
                            ['q1', '']
                        ]
                    },
                },
            },
            initial_state='q0',
            initial_stack_symbol='Z',
            final_states=['q2']
        ),
        
                "aMbN_mGeN":
        # L = {a^m b^n : m >= n >= 0}
        PDA(
            states=['q0', 'q1', 'q2', 'qf'],
            input_symbols=['a', 'b'],
            stack_symbols=['A', 'Z'],
            transitions={
                'q0': {
                    '': {
                        'Z': [
                            ['qf', 'Z']
                        ],
                        'A': [
                            ['q2', '']
                        ],
                    },
                    'a': {
                        'Z': [
                            ['q0', ['A', 'Z']]
                        ],
                        'A': [
                            ['q0', ['A', 'A']]
                        ],
                    },
                    'b': {
                        'A': [
                            ['q1', '']
                        ]
                    },
                },
                'q1': {
                    'b': {
                        'A': [
                            ['q1', '']
                        ]
                    },
                    '': {
                        'A': [
                            ['q2', '']
                        ],
                        'Z': [
                            ['qf', 'Z']
                        ],
                    },
                },
                'q2': {
                    '': {
                        'A': [
                            ['q2', '']
                        ],
                        'Z': [
                            ['qf', 'Z']
                        ],
                    },
                },
            },
            initial_state='q0',
            initial_stack_symbol='Z',
            final_states=['qf']
        ),

        "balancedParens":
        # L = { balanced parentheses }
        PDA(
            states=['q0', 'qf'],
            input_symbols=['(', ')'],
            stack_symbols=['A', 'Z'],
            transitions={
                'q0': {
                    '': {
                        'Z': [
                            ['qf', 'Z']
                        ],
                    },
                    '(': {
                        'Z': [
                            ['q0', ['A', 'Z']]
                        ],
                        'A': [
                            ['q0', ['A', 'A']]
                        ],
                    },
                    ')': {
                        'A': [
                            ['q0', '']
                        ],
                    },
                },
            },
            initial_state='q0',
            initial_stack_symbol='Z',
            final_states=['qf']
        ),

        "aNbNcM":
        # L = {a^n b^n c^m : n,m >= 0}
        PDA(
            states=['q0', 'q1', 'q2', 'qf'],
            input_symbols=['a', 'b', 'c'],
            stack_symbols=['A', 'Z'],
            transitions={
                'q0': {
                    'a': {
                        'Z': [
                            ['q0', ['A', 'Z']]
                        ],
                        'A': [
                            ['q0', ['A', 'A']]
                        ],
                    },
                    'b': {
                        'A': [
                            ['q1', '']
                        ]
                    },
                    '': {
                        'Z': [
                            ['q2', 'Z']
                        ],
                    },
                },
                'q1': {
                    'b': {
                        'A': [
                            ['q1', '']
                        ],
                    },
                    '': {
                        'Z': [
                            ['q2', 'Z']
                        ],
                    },
                },
                'q2': {
                    'c': {
                        'Z': [
                            ['q2', 'Z']
                        ],
                    },
                    '': {
                        'Z': [
                            ['qf', 'Z']
                        ],
                    },
                },
            },
            initial_state='q0',
            initial_stack_symbol='Z',
            final_states=['qf']
        ),

        "equalAsBsAnyOrder":
        # L = {w in {a,b}* : #a = #b}
        PDA(
            states=['q0', 'qf'],
            input_symbols=['a', 'b'],
            stack_symbols=['A', 'B', 'Z'],
            transitions={
                'q0': {
                    'a': {
                        'Z': [
                            ['q0', ['A', 'Z']]
                        ],
                        'A': [
                            ['q0', ['A', 'A']]
                        ],
                        'B': [
                            ['q0', '']
                        ],
                    },
                    'b': {
                        'Z': [
                            ['q0', ['B', 'Z']]
                        ],
                        'B': [
                            ['q0', ['B', 'B']]
                        ],
                        'A': [
                            ['q0', '']
                        ],
                    },
                    '': {
                        'Z': [
                            ['qf', 'Z']
                        ],
                    },
                },
            },
            initial_state='q0',
            initial_stack_symbol='Z',
            final_states=['qf']
        ),

        "aNbN_or_aNb2N":
        # L = {a^n b^n} U {a^n b^(2n)}
        PDA(
            states=['q0', 'q1', 'q2', 'q3', 'qf'],
            input_symbols=['a', 'b'],
            stack_symbols=['A', 'Z'],
            transitions={
                'q0': {
                    '': {
                        'Z': [
                            ['qf', 'Z']
                        ],
                        'A': [
                            ['q1', 'A'],
                            ['q2', 'A']
                        ],
                    },
                    'a': {
                        'Z': [
                            ['q0', ['A', 'Z']]
                        ],
                        'A': [
                            ['q0', ['A', 'A']]
                        ],
                    },
                },
                'q1': {
                    'b': {
                        'A': [
                            ['q1', '']
                        ],
                    },
                    '': {
                        'Z': [
                            ['qf', 'Z']
                        ],
                    },
                },
                'q2': {
                    'b': {
                        'A': [
                            ['q3', 'A']
                        ],
                    },
                    '': {
                        'Z': [
                            ['qf', 'Z']
                        ],
                    },
                },
                'q3': {
                    'b': {
                        'A': [
                            ['q2', '']
                        ],
                    },
                },
            },
            initial_state='q0',
            initial_stack_symbol='Z',
            final_states=['qf']
        )
    }

    def get_lang(self, s):
        return self.languages[s]