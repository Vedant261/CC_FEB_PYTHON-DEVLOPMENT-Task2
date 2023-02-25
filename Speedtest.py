import time

def typing_speed_test():
    quote = "The quick brown fox jumps over the lazy dog"
    print("Type this: '", quote, "'")

    input_string = input()

    start_time = time.time()
    correct_chars = 0
    for i in range(min(len(quote), len(input_string))):
        if quote[i] == input_string[i]:
            correct_chars += 1
    end_time = time.time()

    typing_speed = correct_chars / (end_time - start_time) * 60
    accuracy = correct_chars / len(quote) * 100

    print("Your typing speed is", round(typing_speed, 2), "words per minute")
    print("Your accuracy is", round(accuracy, 2), "%")

if __name__ == "__main__":
    typing_speed_test()
