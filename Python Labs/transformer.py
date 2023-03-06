"""
CSCI-603 - Homework 4
Author: Arya Girisha Rao(ar1422@rit.edu)
        Pradeep Kumar Gontla(pg3328@rit.edu)

This is a python file for Homework 4 to implement program to Encrypt and Decrypt message using four transformations.

New transformation added 'M' - called move the middle character. Represented by just 'M'. Does not has any index value.

We like to make use of famous dialogues. This function moves the middle character by the total count of characters
in dialogue declared as DIALOGUE_FOR_ENCRYPTION.
If the message is even, the middle two characters is moved by the total amount of character in the dialogue
For now, we are using "get to the choppa!" as our dialogue for encryption :). This has 18 characters.

if the message is 'SAS' and the operation is 'M' -> it moves the character 'A' by 18 characters resulting in 'SSS'
if the message is 'ABBA' and the operation is 'M' -> it moves the characters 'BB' by 18 characters resulting in 'ATTA'

"""

DIALOGUE_FOR_ENCRYPTION = "GET TO THE CHOPPA!"


def get_total_length_of_dialogue():
    """
    Function to get the length of the DIALOGUE_FOR_ENCRYPTION
    :return: Sum of total ord of all the characters in the mesaage string
    """
    return len(DIALOGUE_FOR_ENCRYPTION)


def change_the_middle_transformation(message, operation_string, is_encryption):
    """
    Function to change the middle character.
    Moves the middle character(s) based on length by total length of the characters in the DIALOGUE_FOR_ENCRYPTION.
    :param message: message to perform swap transformation.
    :param operation_string: is not used. Always empty String.Keeping it to keep it consistent and call the function.
    :param is_encryption: Whether the operation is encryption or not. True for encryption and False for decryption.
    :return:
    """

    total_length_of_dialogue = get_total_length_of_dialogue()
    if len(message) % 2:
        middle_index = (len(message)) // 2
        shifted_char = shift_transformation(message[middle_index], '0,' + str(total_length_of_dialogue), is_encryption)
        return message[:middle_index] + shifted_char + message[(middle_index + 1):]
    else:
        middle_index = (len(message)) // 2
        shifted_char_1 = shift_transformation(message[middle_index - 1], '0,' + str(total_length_of_dialogue),
                                              is_encryption)
        shifted_char_2 = shift_transformation(message[middle_index], '0,' + str(total_length_of_dialogue),
                                              is_encryption)
        return message[:(middle_index - 1)] + shifted_char_1 + shifted_char_2 + message[(middle_index + 1):]


def get_index_details_from_operation_string(operation_string):
    """
    Function to get the indexes from the operation String.
    The operation String can contain 1 or 2 index based on the Situation.
    To keep it consistent, the code always return 2 values: i, j.
    if j is missing from the operation string, default value 1 is returned for j.
    :param operation_string: String of the format - N or N,M where N and M are numeric values.
    :return: Tuple of values i, j.
    """

    index_list = operation_string.split(',')
    if len(index_list) == 1:
        return int(index_list[0]), 1
    else:
        return int(index_list[0]), int(index_list[1])


def validate_and_update_shifted_index(shifted_ord):
    """
    Function to validate the ordinance value of the shifted Index.
    Checks the shifted ordinance against ord('Z') since Z is the last character.
    If the value is bigger, takes the modulus and puts it back in range(ord('A'), ord('Z'))
    :return: Shifted ordinance in range(ord('A'), ord('Z'))
    """
    max_value_possible = ord('Z')
    min_value = ord('A')
    if shifted_ord > max_value_possible:
        return (shifted_ord % max_value_possible) + min_value + 1
    else:
        return shifted_ord


def shift_transformation(message, operation_string, is_encryption):
    """
    Shifts the letter at given index by n letter
    Allowed format -> 'Sn' or 'Sn, k'where n is positive and k can be positive or negative .
    when the input is 'Sn' -> it's defaulted to 'Sn,1'.
    if Sn,k is for the Encryption, Sn,-k is for Decryption.
    if Sn,-k is for the Encryption, Sn,k is for Decryption.
    Divides the message into 3 - message[:n], message[n], message[n+1:].
    Shifts the message[n] by k, checks if it's within acceptable range.
    returns message[:n] + shifted_message[n] + message[n+1:]

    :param message: message to perform rotate transformation
    :param operation_string: details about the indexes i,j
    :param is_encryption: boolean indicating whether the operation is encryption or decryption.
    :return: String that is transformed using Shift by operating based on operation_string.
    """

    index_value, power_value = get_index_details_from_operation_string(operation_string)
    power_value = power_value % 26
    if not is_encryption:
        power_value = -1 * power_value

    shifted_ord = ord(message[index_value]) + power_value
    shifted_ord = validate_and_update_shifted_index(shifted_ord)
    shifted_char = chr(shifted_ord)
    return message[:index_value] + shifted_char + message[index_value + 1:]


def rotate_transformation(message, operation_string, is_encryption=True):
    """
    Rotates the String by n position
    Allowed format -> 'R' or 'Ri' where i can be positive or negative Integer.
    when the operation is 'R' -> it's defaulted to 'R1'.
    if Ri is for the Encryption, R-i is for Decryption.
    if R-i is for the Encryption, Ri is for Decryption.
    Divides the message in 2 and combines in reverse-> message[-i:], message[:-i]
    :param message: message to perform rotate transformation
    :param operation_string: details about the index i
    :param is_encryption: boolean indicating whether the operation is encryption or decryption.
    :return: String that is transformed using Rotation by operating based on operation_string.
    """
    i = int(operation_string) % len(message) if operation_string else 1
    multiplier = 1 if is_encryption else -1
    i = i * multiplier
    return message[-i:] + message[:-i]


def duplicate_transformation(message, operation_string, is_encryption=True):
    """
    Duplicates the letter at given index
    Allowed format -> 'Dn' or 'Dn, m' where n, m are positive Integers
    when the operation in 'Dn' -> it's defaulted to 'Dn,1'.
    String is divided into message[:(i+1)] + message[i] repeated j times + message[(i+1):]
    in case of decryption, the repeated string between index (i+1) and (i+j+1) is ignored.

    :param message: message to perform duplicate transformation.
    :param operation_string: details about the indexes i, j
    :param is_encryption: boolean indicating whether the operation is encryption or decryption.
    :return:String that is transformed using Duplication by operating based on operation_string.
    """
    i, j = get_index_details_from_operation_string(operation_string)
    if is_encryption:
        return message[:(i + 1)] + message[i] * j + message[(i + 1):]
    else:
        return message[:(i + 1)] + message[(i + j + 1):]


def get_index_details_for_swap_transformation(operation_string, message_length):
    """
    Function to get indexes for Swap transformation.  For swap transformation, there can be 2 or 3 information.
    If 'g' is present, it'll be enclosed in the (). -> (g)i, j -> Eg: (4)2,0.
    If 'g' is not present, it'll be i,j, 1. -> i,j, 1
    :param operation_string: Operation string containing information about i,j,g needed for Swap transformation
    :param message_length: Length of the Message that is about to be transformed.
    :return: Tuple of i, j, and len(message)/g -> (i, j, len/g)
    """
    operation_string = operation_string.replace('(', '').replace(')', ',')
    index_list = operation_string.split(',')
    if len(index_list) == 3:
        return int(index_list[1]), int(index_list[2]), message_length // int(index_list[0])
    else:
        return int(index_list[0]), int(index_list[1]), message_length // message_length


def swap_transformation(message, operation_string, is_encryption=True):
    """
    Swaps the letter at given indexes m and n letter
    Allowed format -> 'Ti,j' or 'T(g)i,j'where i, j, g are positive integers and i<j.
    when the input is 'Ti,j' -> it's defaulted to 'T(1)1,1'.
    The string is converted into list of g equal parts.
    After swapping in the list, the Strings are joined again and final message is returned.
    For eg. if g = 1 and message is 'HELLO', it's converted to ['H','E', 'L', 'L', O']
    if g = 2, and the message is 'ANSWER', it's converted to ['ANS', 'WER']
    Swap case is same for both Encryption and decryption.
    Since the indexes are same both in case of Encryption and Decryption, no change is required.

    :param operation_string: details about the indexes i, j, g of the form (g)i,j
    :param message: message to perform swap transformation.
    :param is_encryption: is not used. Since the swap happens between the two indexes irrespective of E or D.
    :return:String that is transformed using Swap by operating based on operation_string.
    """
    i, j, g = get_index_details_for_swap_transformation(operation_string, len(message))
    split_string = [message[idx: idx + g] for idx in range(0, len(message), g)]
    split_string[i], split_string[j] = split_string[j], split_string[i]
    return ''.join(split_string)


def transform(message_line, operation_line, is_encryption):
    """
    Function to transform the message line using operation line.
    For each operation separated by ';', decides which method to run to perform the transformation.
    Calls the selected function by passing message, operation details, and boolean for encryption or decryption.
    :param message_line: Message line to transform. Message can be encrypted or decrypted.
    :param operation_line: List of operations to perform on the input message in String format.
    :param is_encryption: Whether the operation is encryption or not. True for encryption and False for decryption.
    :return: Transformed message generated by running the List of operations on Message line.
    """
    transformation_map_function = {'S': shift_transformation, 'R': rotate_transformation,
                                   'D': duplicate_transformation, 'T': swap_transformation,
                                   'M': change_the_middle_transformation}

    operations = operation_line.split(';')
    transformed_message = message_line

    if not is_encryption:
        operations.reverse()

    for operation in operations:
        operation_type = operation[0]
        transformed_message = transformation_map_function.get(operation_type)(transformed_message, operation[1:],
                                                                              is_encryption)
    return transformed_message


def get_file_name_details():
    """
    Function to get the file names for message file, operation file, output file from the user.
    :return: Tuple of message file name, operation file name, output file name.
    """

    message_file_name = input("Enter message file name:")
    operation_file_name = input("Enter operation file name:")
    output_file_name = input("Enter output file name:")
    return message_file_name, operation_file_name, output_file_name


def get_encryption_or_decryption_information():
    """
    Function to get the operation details from User.
    User has to select whether he wants to perform Encryption or Decryption on the messages
    :return: Boolean if the operation is Encryption. True if Encryption and False if decryption.
    """
    encrypt_or_decrypt = input("(E)ncrypt or (D)ecrypt?:")
    encrypt_or_decrypt = encrypt_or_decrypt.strip()
    return encrypt_or_decrypt == 'E'


def display_transformed_message(message):
    """
    Function to display the transformed message in the standard output.
    :return: None
    """
    print(message)


def simulate_transformation():
    """
    Function to simulate transformation. Performs below steps as part of the simulation.
    1. Gets file names for messages, operations, write output from user.
    2. Reads message lines and operation lines from message file and operation file in parallel.
    3. Assumption is that the number of lines in message file and operation file is same.
    4. Gets confirmation from user whether the operation is encryption or decryption.
    4. Performs all the transformations specified in each line for every message line.
    5. Prints the transformed message on the Standard output and inserts the data in the file.
    :return: None
    """
    message_file, operation_file, output_file = get_file_name_details()
    is_encryption = get_encryption_or_decryption_information()

    with open(message_file, 'r') as msg, open(operation_file, 'r') as op, open(output_file, 'a') as out:
        for (message_line, operation_line) in zip(msg, op):
            transformed_message = transform(message_line.strip(), operation_line.strip(), is_encryption)
            display_transformed_message(transformed_message)
            out.write(transformed_message)
            out.write("\n")


def main():
    """
    Main function.
    :return: None
    """
    simulate_transformation()


if __name__ == '__main__':
    main()
