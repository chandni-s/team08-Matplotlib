from trello import TrelloApi
import datetime, os

SPRINT_BACKLOG = 'Sprint Backlog'
SPRINT_IN_PROGRESS = 'In Progress'
SPRINT_COMPLETE = 'Sprint Complete'
DATA_FILE = '../docs/data/data.tsv'
DATA_DELIM = '\t'

backlog_list = None
in_progress_list = None
complete_list = None
total_sp = 0

backlog_cards = []
in_progress_cards = []
complete_cards = []


class Card(object):
    '''A trello card'''

    def __init__(self, data):
        '''(Card, dict)
        Initializes a Trello Card Object
        '''
        self.data = data

        name = data['name']

        # Gets the story points for this card and set it
        # cp - current points to track progress
        # tp - total points
        self.cp = 0
        self.tp = 0
        points_str = name[name.find("(")+1:name.find(")")]

        points_split = points_str.split("/")
        if len(points_split) > 1:
            cur_points = points_split[0].strip()
            tot_points = points_split[1].strip()

            if cur_points.isdigit():
                self.cp = int(cur_points)
            if tot_points.isdigit():
                self.tp = int(tot_points)

        # Get the priority of this card and set it
        self.priority = None
        priority_str = name[name.find("[")+1:name.find("]")].lower()
        if priority_str in ['high', 'medium', 'low']:
            self.priority = priority_str

        self.name = name[max(name.find(")") + 1, name.find("]") + 1):].strip()


    def __str__(self):
        '''(Card) -> str
        Returns the string representation of the Trello Card
        '''
        return self.name

    def __repr__(self):
        '''(Card) -> str
        Returns the string representation of the Trello Card
        '''
        return self.name


def get_lists(lists):
    '''(list of dict) -> None
    Gets data for Backlog List, In Progress List and Completed List
    and set their respective global variables.
    '''
    global backlog_list
    global in_progress_list
    global complete_list
    for lis in lists:
        if lis['name'] == SPRINT_BACKLOG:
            backlog_list = lis
        elif lis['name'] == SPRINT_IN_PROGRESS:
            in_progress_list = lis
        elif lis['name'] == SPRINT_COMPLETE:
            complete_list = lis


def get_sprint_cards(cards):
    '''(list of dict) -> None
    Updates the lists backlog_cards, in_progress_cards and
    complete_cards.
    '''
    global total_sp
    for card in cards:
        cardObj = Card(card)
        if (card['idList'] == backlog_list['id']):
            backlog_cards.append(cardObj)
            total_sp += cardObj.tp
        elif (card['idList'] == in_progress_list['id']):
            in_progress_cards.append(cardObj)
            total_sp += cardObj.tp
        elif (card['idList'] == complete_list['id']):
            complete_cards.append(cardObj)
            total_sp += cardObj.tp


def update_data_file():
    '''() -> None
    Updates the DATA_FILE with the latest information about the
    current sprint from trello
    '''
    if (not(os.path.exists(DATA_FILE))):
        data_file = open(DATA_FILE, 'w')
        data_file.write('date\tleftover\n')
        data_file.close()

    data_file = open(DATA_FILE, 'r')
    lines = data_file.readlines()
    data_file.close()

	# Calculate burn down values

    burned = 0
    for card in in_progress_cards:
        burned += card.cp

    for card in complete_cards:
        burned += card.tp

    total_sp = 0
    for card in backlog_cards + in_progress_cards + complete_cards:
        total_sp += card.tp

    try:
        # Make sure there is a newline at the end of each line
        for i in range(len(lines)):
            lines[i] = lines[i].strip() + '\n'

        # Add data to data file if not already present
        last_en = lines[-1]

        last_en_spl = last_en.split(DATA_DELIM)
        date_tod = datetime.date.today().strftime("%d-%b-%y")

        if not(last_en_spl[0] == date_tod):
            lines.append(date_tod + DATA_DELIM + str(total_sp - burned) + '\n')
        else:
            lines.append(last_en_spl[0] + DATA_DELIM + str(total_sp - burned) + '\n')

        data_file = open(DATA_FILE, 'w')
        data_file.writelines(lines)
        data_file.close()

    except RuntimeError as re:
        print re


def main():
    '''() -> None
    Reads information from trello board and generates a TSV file
    for burndown chart generation.
    '''
    config = open('config', 'r')
    contents = config.readlines()
    config.close()

    os.chdir('../docs')

    TRELLO_APP_KEY = contents[0].strip().split('=')[1]
    TRELLO_SERVER_TOKEN = contents[1].strip().split('=')[1]
    TRELLO_BOARD_ID = contents[2].strip().split('=')[1]

    trello = TrelloApi(TRELLO_APP_KEY)
    trello.set_token(TRELLO_SERVER_TOKEN)
    boards = trello.boards.get(TRELLO_BOARD_ID)
    lists = trello.boards.get_list(TRELLO_BOARD_ID)
    cards = trello.boards.get_card(TRELLO_BOARD_ID)
    actions = trello.boards.get_action(TRELLO_BOARD_ID)

    get_lists(lists)
    get_sprint_cards(cards)

    if (not(backlog_list and in_progress_list and complete_list)):
        print ('Backlog List, In Progress List and Complete List must be made.')
        exit()

    update_data_file()


if (__name__ == '__main__'):
    main()
