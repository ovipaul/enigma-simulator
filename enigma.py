
def rotate(list, no_rotation):
    return list[no_rotation:] + list[:no_rotation]

def message_processor(message):
    message = message.upper()
    message = message.replace(" ", "")
    return message
def select_rotor(rotor_model):
    rotor_i_list  =    ['E','K','M','F','L','G','D','Q','V','Z','N','T','O','W','Y','H','X','U','S','P','A','I','B','R','C','J']
    rotor_ii_list =    ['A','J','D','K','S','I','R','U','X','B','L','H','W','T','M','C','Q','G','Z','N','P','Y','F','V','O','E']
    rotor_iii_list =   ['B','D','F','H','J','L','C','P','R','T','X','V','Z','N','Y','E','I','W','G','A','K','M','U','S','Q','O']
    rotor_iv_list =    ['E','S','O','V','P','Z','J','A','Y','Q','U','I','R','H','X','L','N','F','T','G','K','D','C','M','W','B']   
    rotor_v_list =     ['V','Z','B','R','G','I','T','Y','U','P','S','D','N','H','L','X','A','W','M','J','Q','O','F','E','C','K']
    rotor_vi_list =    ['J','P','G','V','O','U','M','F','Y','Q','B','E','N','H','Z','R','D','K','A','S','X','L','I','C','T','W']
    rotor_vii_list =   ['N','Z','J','H','G','R','C','X','M','Y','S','W','B','O','U','F','A','I','V','L','P','E','K','Q','D','T']
    rotor_viii_list =  ['F','K','Q','H','T','L','X','O','C','B','J','S','P','D','Z','R','A','M','E','W','N','I','U','Y','G','V']
    rotor_beta_list =  ['L','E','Y','J','V','C','N','I','X','W','P','B','Q','M','D','R','T','A','K','Z','G','F','U','H','O','S']
    rotor_gamma_list = ['F','S','O','K','A','N','U','E','R','H','M','B','T','I','Y','C','W','L','Q','P','Z','X','V','G','J','D']
    if rotor_model == 'Rotor-I':
        rotor_model_list = rotor_i_list
    elif rotor_model == 'Rotor-II':
        rotor_model_list = rotor_ii_list
    elif rotor_model == 'Rotor-III':
        rotor_model_list = rotor_iii_list
    elif rotor_model == 'Rotor-IV':
        rotor_model_list = rotor_iv_list
    elif rotor_model == 'Rotor-V':
        rotor_model_list = rotor_v_list
    elif rotor_model == 'Rotor-VI':
        rotor_model_list = rotor_vi_list
    elif rotor_model == 'Rotor-VII':
        rotor_model_list = rotor_vii_list
    elif rotor_model == 'Rotor-VIII':
        rotor_model_list = rotor_viii_list
    elif rotor_model == 'Rotor-Beta':
        rotor_model_list = rotor_beta_list
    else:
        rotor_model_list = rotor_gamma_list
    return rotor_model_list

def select_reflector(reflector_model):
    reflector_b_list =      ['Y','R','U','H','Q','S','L','D','P','X','N','G','O','K','M','I','E','B','F','Z','C','W','V','J','A','T']
    reflector_c_list =      ['F','V','P','J','I','A','O','Y','E','D','R','Z','X','W','G','C','T','K','U','Q','S','B','N','M','H','L']
    reflector_b_thin_list = ['E','N','K','Q','A','U','Y','W','J','I','C','O','P','B','L','M','D','X','Z','V','F','T','H','R','G','S']
    reflector_c_thin_list = ['R','D','O','B','J','N','T','K','V','E','H','M','L','F','C','W','Z','A','X','G','Y','I','P','S','U','Q']
    
    if reflector_model == 'Reflector-B':
        reflector_model_list = reflector_b_list
    elif reflector_model == 'Reflector-C':
        reflector_model_list = reflector_c_list
    elif reflector_model == 'Reflector-B Thin':
        reflector_model_list = reflector_b_thin_list
    else:
        reflector_model_list = reflector_c_thin_list

    return reflector_model_list
def starter(rotor_list, starter_letter):
    starter_index = rotor_list.index(starter_letter)
    rotor_list = rotate(rotor_list,starter_index)
    return rotor_list

def enigma(message, rotor_slection, reflector_selection, starter_list):   
    keyboard_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    
    message = message_processor(message)
    first_rotor_counter = 0
    second_rotor_counter = 0
    third_rotor_counter = 0
    encrypted_message=""

    first_rotor_list = select_rotor(rotor_slection[0])
    first_rotor_list = starter(first_rotor_list,starter_list[0])

    second_rotor_list = select_rotor(rotor_slection[1])
    second_rotor_list = starter(second_rotor_list,starter_list[1])
    
    third_rotor_list = select_rotor(rotor_slection[2])
    third_rotor_list = starter(third_rotor_list,starter_list[2])

    reflector_list = select_reflector(reflector_selection)
    for letter in message:
        #Encrypting Message
        keyboard = keyboard_list.index(letter)
        first_rotor = first_rotor_list[keyboard]

        keyboard = keyboard_list.index(first_rotor)
        second_rotor = second_rotor_list[keyboard]

        keyboard = keyboard_list.index(second_rotor)
        third_rotor = third_rotor_list[keyboard]

        #Reflector
        keyboard = keyboard_list.index(third_rotor)
        reflector = reflector_list[keyboard]


        #Rotar backtracking
        third_rotor = third_rotor_list.index(reflector)
        keyboard = keyboard_list[third_rotor]

        second_rotor = second_rotor_list.index(keyboard)
        keyboard = keyboard_list[second_rotor]
        
        first_rotor = first_rotor_list.index(keyboard)
        keyboard = keyboard_list[first_rotor]
        
        #Putting the encrypted letters together in a list
        encrypted_message+=keyboard


        #Rotating list according to counts
        first_rotor_list = rotate(first_rotor_list,1)
        first_rotor_counter += 1
        if first_rotor_counter == 25:
            second_rotor_list = rotate(second_rotor_list,1)
            second_rotor_counter += 1

        if second_rotor_counter == 25:
            third_rotor_list = rotate(third_rotor_list,1)
            third_rotor_list += 1


    return encrypted_message