from collections import defaultdict, namedtuple, Counter

Tracker = namedtuple('Tracker', ['i','j', 'visited', 'acc'])

DEBUG = False

def dprint(string_to_print):
    if DEBUG:
        print(string_to_print)

class Solution:


    def build_tracker(self, i, j, m, letter, tracker=None):
        acc = letter
        if tracker == None:
            visited = 0
        else:
            visited = tracker.visited
            acc = tracker.acc + letter

        visited |= 1 << ((i*m)+j)
        return Tracker(i, j, visited, acc)

    def is_valid_move(self, board, next_letter, i, j, tracker):
        if i < 0 or i == len(board) or j < 0 or j == len(board[0]):
            dprint(f"Move to {i},{j} was out of bounds")
            return False

        visited_location = tracker.visited & (1 << ((i*len(board[0])+j)))
        dprint(f"Tracker marked {i},{j} as {visited_location}")
        dprint(f"Next letter is {next_letter}")

        return not visited_location and next_letter == board[i][j]

    def get_valid_moves(self, board, word, tracker):
        valid_moves = []
        if len(word) == len(tracker.acc):
            return valid_moves

        m = len(board[0])
        next_letter = word[len(tracker.acc)]
        if self.is_valid_move(board, next_letter, tracker.i-1, tracker.j, tracker):
                valid_moves.append(self.build_tracker(tracker.i-1, tracker.j, m, next_letter, tracker))

        if self.is_valid_move(board, next_letter, tracker.i+1, tracker.j, tracker):
                valid_moves.append(self.build_tracker(tracker.i+1, tracker.j, m, next_letter, tracker))

        if self.is_valid_move(board, next_letter, tracker.i, tracker.j-1, tracker):
                valid_moves.append(self.build_tracker(tracker.i, tracker.j-1, m, next_letter, tracker))

        if self.is_valid_move(board, next_letter, tracker.i, tracker.j+1, tracker):
                valid_moves.append(self.build_tracker(tracker.i, tracker.j+1, m, next_letter, tracker))


        return valid_moves


    def exist(self, board: List[List[str]], word: str) -> bool:
        starting_positions = []

        m = len(board[0])
        n = len(board)

        board_char_counts = Counter(sum(board, []))
        word_char_counts = Counter(word)

        for char in word:
            if word_char_counts[char] > board_char_counts[char]:
                return False

        if word_char_counts[word[-1]] < word_char_counts[word[0]]:
            word = word[::-1]

        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    starting_positions.append((i, j))
        
        
        if len(starting_positions) == 0:
            return False


        queue = [self.build_tracker(*starting_position, len(board[0]), word[0]) for starting_position in starting_positions]

        while len(queue) > 0:
            current = queue.pop(0)
            dprint(current)
            valid_moves = self.get_valid_moves(board, word, current)
            if len(valid_moves) == 0 and current.acc == word:
                return True

            dprint(f"Found {len(valid_moves)} valid moves")
            queue += valid_moves

        return False

                
                
                

                




        
