import math
import os


def stopword(wstr):
    w = wstr.strip()
    if len(w) < 4:
        return True
    return False


def read_dir(dirn):
    cont_l = []
    for fn in os.listdir(dirn):
        with open(os.path.join(dirn, fn), encoding="latin-1") as f:
            words = [w.strip()
                for w in f.read().replace("\n", " ").split(" ")
                    if not stopword(w)
            ]
            cont_l.append(words)
    return cont_l


def count_probabilities(hams, spams):
    number_of_messages = hams + spams

    return hams / number_of_messages, spams / number_of_messages


def count_word_frequency(messages):
    words = []
    for message in messages:
        words.extend(message)

    word_frequency = {}
    for word in words:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1

    return word_frequency


def count_words(messages):
    words = []
    for message in messages:
        words.extend(message)

    return len(words)


def get_unique_words(hams, spams):
    words = []
    for message in hams:
        words.extend(message)

    for message in spams:
        words.extend(message)

    return set(words)


if __name__ == '__main__':
    ham_l = read_dir("enron6\\ham")
    spam_l = read_dir("enron6\\spam")

    number_of_hams = len(ham_l)
    number_of_spams = len(spam_l)

    ham_probability, spam_probability = count_probabilities(number_of_hams, number_of_spams)

    ham_word_frequency = count_word_frequency(ham_l)
    spam_word_frequency = count_word_frequency(spam_l)

    number_of_ham_words = count_words(ham_l)
    number_of_spam_words = count_words(spam_l)

    unique_words_from_training = get_unique_words(ham_l, spam_l)
    V = len(unique_words_from_training)

    # ----------------------------------------------

    custom_message_1 = read_dir("test\\message1")[0]
    unique_words = set(custom_message_1)

    custom_message_words_1 = []
    for word in unique_words:
        if word in unique_words_from_training:
            custom_message_words_1.append(word)

    # count ham for message 1
    h_ham = math.log(ham_probability)
    for w in custom_message_words_1:
        if w in ham_word_frequency:
            h_ham += math.log((ham_word_frequency[w] + 1) / (number_of_ham_words + V))
        else:
            h_ham += math.log(1 / (number_of_ham_words + V))
    print('Message #1, HAM:', h_ham)

    # count spam for message 1
    h_spam = math.log(spam_probability)
    for w in custom_message_words_1:
        if w in spam_word_frequency:
            h_spam += math.log((spam_word_frequency[w] + 1) / (number_of_spam_words + V))
        else:
            h_spam += math.log(1 / (number_of_spam_words + V))
    print('Message #1, SPAM:', h_spam)

    # ----------------------------------------------

    custom_message_2 = read_dir("test\\message2")[0]
    unique_words = set(custom_message_2)

    custom_message_words_2 = []
    for word in unique_words:
        if word in unique_words_from_training:
            custom_message_words_2.append(word)

    # count ham for message 2
    h_ham = math.log(ham_probability)
    for w in custom_message_words_2:
        if w in ham_word_frequency:
            h_ham += math.log((ham_word_frequency[w] + 1) / (number_of_ham_words + V))
        else:
            h_ham += math.log(1 / (number_of_ham_words + V))
    print('Message #2, HAM:', h_ham)

    # count spam for message 2
    h_spam = math.log(spam_probability)
    for w in custom_message_words_2:
        if w in spam_word_frequency:
            h_spam += math.log((spam_word_frequency[w] + 1) / (number_of_spam_words + V))
        else:
            h_spam += math.log(1 / (number_of_spam_words + V))
    print('Message #2, SPAM:', h_spam)
