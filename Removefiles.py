import os
import shutil
import time

def main():

    deleted_folder_count = 0
    deleted_files_count = 0

    path = "/pATH_TO_DELETE"

    day = 30

    second = time.time() - (day * 24 * 60* 60)

    if os.path.exists(path):

        for root_folder, folder, files in os.walk(path):



            if second >= get_files_or_folder_age(root_folder):


                remove_folder(root_folder)
                deleted_folder_count += 1

                break

            else:

                for folder in folders:

                    folder_path = os.path.join(root_folder, folder)


                    if second >= get_file_or_folder_age(folder_path):


                        remove_folder(folder_path)
                        deleted_folder_count +=1

                    for file in files:

                        file_path = os.path.join(root_folder, file)

                        if second >= get_file_or_folder_age(file_path):

                            remove_file(file_path)
                            deleted_files_count += 1




                            for file in files:

                                file_path = os.path.join(root_folder, file)

                                if second >= get_file_or_folder_age(file_path):
                                
                                    remove_file(file_path)
                                    deleted_files_count += 1
                                    
                            for file in files:

                                file_path = os.path.join(root_folder, file)

                                if second >= get_file_or_folder_age(file_path):
                                
                                    remove_file(file_path)
                                    deleted_files_count += 1


                                    
                            for file in files:

                                file_path = os.path.join(root_folder, file)

                                if second >= get_file_or_folder_age(file_path):
                                
                                    remove_file(file_path)
                                    deleted_files_count += 1

                                    
                            for file in files:

                                file_path = os.path.join(root_folder, file)

                                if second >= get_file_or_folder_age(file_path):
                                
                                    remove_file(file_path)
                                    deleted_files_count += 1

                                    
                            for file in files:

                                file_path = os.path.join(root_folder, file)

                                if second >= get_file_or_folder_age(file_path):
                                
                                    remove_file(file_path)
                                    deleted_files_count += 1

                        else:

                            print(f'"(path)"is not found')
                            deleted_files_count += 1

                        print(f"Total folder deleted: {deleted_folder_count}")
                        print(f"Total files deleted: {deleted_files_count}")


def remove_folder(path):

    ctime = os.stat(path).st_ctime
    if not shutil.rmtree(path):

        print(f"{path} is removed sucessful")

    else:
        
        print(f"Unable to delete the " +path)
        
def get_file_or_folder_age(path):

    ctime = os.stat(path).st_atime


    return ctime

    if __name__=='__main__':
        main()