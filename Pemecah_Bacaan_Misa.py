import re

def main(input):
    # file = open('Sample1.txt', 'r').read().split('\n')
    file = input.split('\n')

    passage = file[0]
    text = file[2]

    char_idx = 0

    initial_state = True
    terminal_state = False
    selection_state = False
    conjunction_split = False

    idx_start = -1
    idx_end = -1

    single_quote = False
    double_quote = False

    terminal_candidate = []
    split_text = []

    char_length = 80

    while char_idx < len(text):
        # print(char_idx)
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
            if char_idx - idx_start <= char_length:
                char_match = re.match('''[.,;:?!"]''', text[char_idx])

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
                    elif text[char_idx] == ',':
                        terminal_candidate.append(char_idx)
            else:
                terminal_state = False
                selection_state = True
                conjunction_split = True

            char_idx += 1

        if selection_state:
            if conjunction_split:
                current_text = text[idx_start:idx_start + char_length].lower()

                conjunction_list = ['dan',
                                    'ataukah'
                                    'serta',
                                    'lagipula',
                                    'lagi pula',
                                    'setelah',
                                    'sejak',
                                    'selanjutnya',
                                    'tetapi',
                                    'tapi',
                                    'melainkan',
                                    'sedangkan',
                                    'atau',
                                    'maupun',
                                    'mau pun',
                                    'untuk',
                                    'agar',
                                    'supaya',
                                    'sebab',
                                    'karena',
                                    'sehingga',
                                    'akibatnya',
                                    'lalu',
                                    'kemudian',
                                    'jika',
                                    'kalau',
                                    'apabila',
                                    'walau',
                                    'meski',
                                    'biar',
                                    'seperti',
                                    'bagai',
                                    'sebagai',
                                    'bahkan',
                                    'yaitu',
                                    'yakni',
                                    'kecuali',
                                    'selain',
                                    'bahwa']

                conjunction_list_pos = [(re.search(r'\s' + word, current_text)) for word in conjunction_list]
                # print(conjunction_list_pos)

                for i in range(len(conjunction_list_pos)):
                    if conjunction_list_pos[i]:
                        terminal_candidate.append(conjunction_list_pos[i].start() + idx_start)

                terminal_candidate.sort()

                idx_end = terminal_candidate[-1]

                if text[idx_end] == ',':                
                    split_text.append(text[idx_start:idx_end])
                else:
                    idx_end -= 1
                    letter_found = False

                    while not(letter_found):
                        if re.match('[a-zA-Z,]', text[idx_end]):
                            if text[idx_end] == ',':
                                split_text.append(text[idx_start:idx_end])
                            else:
                                split_text.append(text[idx_start:idx_end + 1])

                            letter_found = True
                            break

                        idx_end -= 1

                conjunction_split = False
                selection_state = False
                initial_state = True

                char_idx = idx_end + 1
            else:
                idx_end = terminal_candidate[-1]

                if text[idx_end] == '.' or text[idx_end] == ';' or text[idx_end] == ':':
                    split_text.append(text[idx_start:idx_end])
                elif text[idx_end] == '?' or text[idx_end] == '!' or text[idx_end] == '"':
                    split_text.append(text[idx_start:idx_end + 1])

                selection_state = False
                initial_state = True

                char_idx = idx_end + 1
                terminal_candidate.clear()

    split_text = [(element + '\n' + '(' + passage + ')') for element in split_text]

    for i in range(len(split_text)):    
        if re.match('[a-z]', split_text[i][0]):
            first_letter = split_text[i][0].upper()
            sentence = split_text[i][1:]

            split_text[i] = first_letter + sentence

    result = '\n\n'.join(split_text)

    # print(result)
    return result