import hashlib
import os
import shutil
import binascii

mapper = ['00', '01', '02', '03', '04', '05', '06', '07', '08']
key_path = "./key.txt"

def generation_map():
    size = 4
    while (size < 10):
        for index0 in range(len(mapper)):
            temp_path = ""
            temp_path = temp_path + mapper[index0]
            for index1 in range(len(mapper)):
                temp_path = temp_path[0:2]
                if index1 == index0:
                    continue
                else:
                    temp_path = temp_path + mapper[index1]
                    for index2 in range(len(mapper)):
                        temp_path = temp_path[0:4]
                        if index0 == index2 or index1 == index2:
                            continue
                        else:
                            temp_path = temp_path + mapper[index2]
                            for index3 in range(len(mapper)):
                                temp_path = temp_path[0:6]
                                if index0 == index3 or index1 == index3 or index2 == index3:
                                    continue
                                else:
                                    temp_path = temp_path + mapper[index3]
                                    # password is 4 point
                                    write_file(temp_path)

                                    for index4 in range(len(mapper)):
                                        temp_path = temp_path[0:8]
                                        if index0 == index4 or index1 == index4 or index2 == index4 or index3 == index4:
                                            continue
                                        else:
                                            temp_path = temp_path + mapper[index4]
                                            # password is 5 point
                                            write_file(temp_path)

                                            for index5 in range(len(mapper)):
                                                temp_path = temp_path[0:10]
                                                if index0 == index5 or index1 == index5 or index2 == index5 or index3 == index5 or index4 == index5:
                                                    continue
                                                else:
                                                    temp_path = temp_path + mapper[index5]
                                                    # password is 6 point
                                                    write_file(temp_path)

                                                    for index6 in range(len(mapper)):
                                                        temp_path = temp_path[0:12]

                                                        if index0 == index6 or index1 == index6 or index2 == index6 or index3 == index6 or index4 == index6 or index5 == index6:
                                                            continue
                                                        else:
                                                            temp_path = temp_path + mapper[index6]
                                                            # password is 7 point
                                                            write_file(temp_path)

                                                            for index7 in range(len(mapper)):
                                                                temp_path = temp_path[0:14]

                                                                if index0 == index7 or index1 == index7 or index2 == index7 or index3 == index7 or index4 == index7 or index5 == index7 or index6 == index7:
                                                                    continue
                                                                else:
                                                                    temp_path = temp_path + mapper[index7]
                                                                    # password is 8 point
                                                                    write_file(temp_path)

                                                                    for index8 in range(len(mapper)):
                                                                        temp_path = temp_path[0:16]

                                                                        if index0 == index8 or index1 == index8 or index2 == index8 or index3 == index8 or index4 == index8 or index5 == index8 or index6 == index8 or index7 == index8:
                                                                            continue
                                                                        else:
                                                                            temp_path = temp_path + mapper[index8]
                                                                            # password is 9 point

                                                                            write_file(temp_path)

        break


def write_file(temp_path):
    with open(key_path, 'a') as file:
        temp_path = encrypt(temp_path)
        print (temp_path)
        file.writelines(temp_path + '\n')


def encrypt(str):
    hex_sha = hashlib.sha1(str.decode('hex')).hexdigest()
    str = str + '\t' + hex_sha
    return str


if __name__ == '__main__':
    print 'start----'

    if (os.path.isfile(key_path) == False):
        generation_map()
    else:
        print "is exist"
    # print(encrypt("000102050403060708"))
    
    print 'map is under:'
    print '00 01 02'
    print '03 04 05'
    print '06 07 08'
    print 'end'
