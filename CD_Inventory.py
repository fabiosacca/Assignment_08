#------------------------------------------#
# Title: CD_Inventory.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created file
# DBiesinger, 2030-Jan-01, Added pseudocode to complete assignment 08
# fabiosacca, 2022-Dec-04, Completed Todos
#------------------------------------------#

# -- DATA -- #
strFileName = 'cdInventory.txt'
lstOfCDObjects = []

class CD:
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
        
    methods:
        load_cd(file_name, table): --> None
        add_cd(row, table): --> Confirmation message
    """
    # TODone Add Code to the CD class
    # -- Field -- #
    cd_id = None
    cd_title = ''
    cd_artist = ''
    
    # -- Constructor -- #
    def __init__(self, cd_id, cd_title, cd_artist):
        # -- Attributes -- #
        self.__cd_id = cd_id
        self.__cd_title = cd_title
        self.__cd_artist = cd_artist
        
    # -- Properties -- #
    @property
    def cd_id(self,value):
        return self.__cd_id

    def cd_title(self,value):
        return self.__cd_title

    def cd_artist(self,value):
        return self.__cd_artist

    @cd_id.setter
    def cd_id(self,value):
        if str(value).isnan():
            raise Exception('The value must a number')

    @staticmethod
    def load_cd(file_name, table):
        """Function to process user request to load inventory from file

        Confirms user choice before loading inventory data from runtime and deletes all entries in memory

        Args:
            file_name (string): name of file used to write the data from
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            None
        """
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('Type \'yes\' to continue and reload from file. Otherwise reload will be canceled: ')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            table = FileIO.load_inventory(file_name)
            IO.show_inventory(table)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(table)

    @staticmethod
    def add_cd(row, table):

        """Function to manage data ingestion from user input to a list of dictionaries

        Adds data from user entry into a 2D table (list of dicts) in memory during runtime.

        Args:
            data (list): values entered by user for ID, CD Title, Artist Name
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            Confirmation message the CD was added to inventory.
        """
        table.append(row)
        print('The CD was added to Inventory')


# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
        
    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """
    # -- Field -- #
    cd_id = None
    cd_title = ''
    cd_artist = ''
    
    # -- Constructor -- #
    def __init__(self, cd_id, cd_title, cd_artist):
        # -- Attributes -- #
        self.__cd_id = cd_id
        self.__cd_title = cd_title
        self.__cd_artist = cd_artist
        
    # -- Properties -- #
    @property
    def cd_id(self,value):
        return self.__cd_id

    def cd_title(self,value):
        return self.__cd_title

    def cd_artist(self,value):
        return self.__cd_artist

    @cd_id.setter
    def cd_id(self,value):
        if str(value).isnan():
            raise Exception('The value must a number')
    
    # TODone Add code to process data from a file
    @staticmethod
    def load_inventory(file_name):
        """Function to manage data ingestion from file to a list of dictionaries

        Reads the data from file identified by file_name into a 2D table
        (list of dicts) table one line in the file represents one dictionary row in table.

        Args:
            file_name (string): name of file used to read the data from

        Returns:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime
        """
        table = []
        objFile = open(file_name, 'r')
        for line in objFile:
            data = line.strip().split(',')
            dicRow = {'ID': int(data[0]), 'Title': data[1], 'Artist': data[2]}
            table.append(dicRow)
        objFile.close()
        return table
        IO.show_inventory(table)
        
    # TODone Add code to process data to a file    
    @staticmethod
    def save_inventory(file_name, table):
        # ToDONE Add code here
        """Function to manage data storage from a list of dictionaries to a file

        Saves the data to file identified by file_name from a 2D table
        (list of lists).

        Args:
            file_name (string): name of file used to write the data from
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            None.
        """
        while True:
            strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
            if strYesNo == 'y':
                objFile = open(strFileName, 'w')
                for row in table:
                    lstValues = list(row.values())
                    lstValues[0] = str(lstValues[0])
                    objFile.write(','.join(lstValues) + '\n')
                objFile.close()
                break
            elif strYesNo == 'n':
                input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
                break
            else:
                print('Incorrect choice!! Please try again.\n')
                continue

# -- PRESENTATION (Input/Output) -- #
class IO:
    # TODone add docstring
    """Handling Input / Output
    properties:

    methods:
        print_menu(): -> None
        menu_choice(): --> (a lower case sting of the users input out of the choices)
        show_inventory(table): --> None
        get_user_input(): -->  (cd_id, cd_title, cd_artist)
        
    """
    
    # TODone add code to show menu to user
    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
            
        """
        print('\nMenu\n\n[l] Load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[s] Save Inventory to file\n[x] Exit\n')

    # TODone add code to captures user's choice
    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case string of the users input out of the choices l, a, i, d, s or x

        """
        choice = input('Which operation would you like to perform? [l, a, i, s or x]: ').lower().strip()
        while choice not in ['l', 'a', 'i', 's', 'x']:
            print('Invalid choice. Please select one of the options listed.\n')
            choice = input('Which operation would you like to perform? [l, a, i, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice
    
    # TODone add code to display the current data on screen
    @staticmethod
    def show_inventory(table):
        """Displays current inventory table

        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """
        print('\n======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print('{}\t{} (by:{})'.format(*row.values()))
        print('======================================')
        
    # TODone add code to get CD data from user
    @staticmethod
    def get_user_input():
        """ Function to get the user input for adding a CD entry

        The entry will be returned to be used by a DataProcessor function that will Add it to inventory.

        Args:
            None
            
        Returns:
            cd_id (int): User supplied ID for entry
            cd_title (string): Title of CD
            cd_artist (string): Name of artist
        """
        while True:
            cd_id = input('\nEnter ID: ').strip()
            try:
                cd_id = int(cd_id)
                break
            except ValueError as e:
                print('\nThat is not a valid ID number. Please try again.')
                print('\nBuild in error info:', e.__doc__, sep='\n')
            except Exception as e:
                print('\nThere was a general error!')
                print('\nBuild in error info:', e.__doc__, sep='\n')
        cd_title = input('What is the CD\'s title? ').strip()
        cd_artist = input('What is the Artist\'s name? ').strip()
        cd = {'ID': cd_id, 'Title': cd_title, 'Artist': cd_artist}
        return cd
    
# -- Main Body of Script -- #
# TODone Add Code to the main body
# Load data from file into a list of CD objects on script start
lstOfCDObjects = FileIO.load_inventory(strFileName)

# Display menu to user
while True:
    IO.print_menu()
    strChoice = IO.menu_choice()
    
    # show user current inventory
    if strChoice == 'i':
        IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    
    # let user add data to the inventory
    elif strChoice == 'a':
        CD.add_cd(IO.get_user_input(), lstOfCDObjects)
        IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
        
    # let user save inventory to file
    elif strChoice == 's':
        # 3.6.1 Display current inventory and ask user for confirmation to save
        IO.show_inventory(lstOfCDObjects)
        FileIO.save_inventory(strFileName, lstOfCDObjects)
        continue  # start loop back at top
        
    # let user load inventory from file
    elif strChoice == 'l':
        CD.load_cd(strFileName, lstOfCDObjects)
        continue  # start loop back at top.
    
    # let user exit program
    elif strChoice == 'x':
        break

    else:
        print('Invalid choice. Please select one of the options listed.')
        continue  # start loop back at top.
