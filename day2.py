def part1():
    with open("./input_day2_test.txt","r") as file:
        content = file.read()
        ranges = content.split(',')
        non_valid_numbers = []
        result:int = 0
        for each in ranges:
            local_range= each.split('-')
            high_number = int(local_range[1])
            low_number = int(local_range [0])
            number_of_checks = high_number - low_number
            for i in range (number_of_checks+1):
                current_number = str(low_number + i)
                for j in range (len(str(current_number))):
                    if current_number[:j] == current_number[j:]:
                        non_valid_numbers.append(current_number)
        for number in non_valid_numbers:
            result = result + int(number)
    print(result)

def part2():
        with open("./input_day2_test.txt","r") as file:
            content = file.read()
            ranges = content.split(',')
            non_valid_numbers = []
            result:int = 0
            for each in ranges:
                local_range= each.split('-')
                high_number = int(local_range[1])
                low_number = int(local_range [0])
                number_of_checks = high_number - low_number
                for i in range (number_of_checks+1):
                    current_number = str(low_number + i)
                    max_length_number = int(current_number)//2
                    print(f"checking: {current_number} > up to: {max_length_number}",)
                    j = 0 #length counter
                    k = 1
                    temp_string = ""
                    while j < max_length_number:
                        number_being_validated = current_number[:j+1]
                        number_length = len(number_being_validated)
                        next_number = current_number[k:k+number_length]
                        if not next_number:
                            print(f"Skipped {current_number}")
                            break
                        print(f"got: {number_being_validated} > against: {next_number}",)
                        if len(next_number) == number_length and number_being_validated == next_number:
                            non_valid_numbers.append(current_number)
                            j+=1
                            print(f"found {current_number}")
                            break
                        else:
                            j= j+1
                        k = k+1
        print(non_valid_numbers)
if __name__ == '__main__':
    result = part2()