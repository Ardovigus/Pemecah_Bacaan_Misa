import re

file = open('Sample.txt', 'r').read().split('\n')

passage = file[0]
text = file[2]

char_idx = 0

initial_state = True
terminal_state = False
selection_state = False

idx_start = -1
idx_end = -1

single_quote = False
double_quote = False

terminal_candidate = []
split_text = []

while char_idx < len(text):
    if char_idx == len(text) - 1:
        terminal_candidate.append(char_idx)

        initial_state = False
        terminal_state = False
        selection_state = True

        char_idx += 1

    if initial_state:
        char_match = re.match('''[a-zA-Z"]''', text[char_idx])

        if char_match:
            idx_start = char_idx

            initial_state = False
            terminal_state = True

            if text[idx_start] == '"':
                double_quote = True
            # elif text[idx_start] == "'":
            #     single_quote = True

        char_idx += 1

    if terminal_state:
        char_match = re.match('''[.;:?!"]''', text[char_idx])

        if char_match:
            if ((text[char_idx] == '.' or text[char_idx] == '?' or text[char_idx] == '!') and (text[char_idx + 1] != '"')) or (text[char_idx] == ';' or text[char_idx] == ':'):
                terminal_candidate.append(char_idx)

                terminal_state = False
                selection_state = True
            elif text[char_idx] == '"' and double_quote:
                terminal_candidate.append(char_idx)

                double_quote = False

                terminal_state = False
                selection_state = True

        char_idx += 1

    if selection_state:
        idx_end = terminal_candidate[-1]

        if text[idx_end] == '.' or text[idx_end] == ';' or text[idx_end] == ':':
            split_text.append(text[idx_start:idx_end])
        elif text[idx_end] == '?' or text[idx_end] == '!' or text[idx_end] == '"':
            split_text.append(text[idx_start:idx_end + 1])

        selection_state = False
        initial_state = True

        # char_idx = idx_end + 1

split_text = [(element + '\n' + '(' + passage + ')') for element in split_text]

result = '\n\n'.join(split_text)

print(result)