from typing import List


class Piece:
    """A piece for playing a game on a chess GameBoard.

    === Attributes ===
    position:
        A tuple referring to the row and column where the piece currently is.
    allowed_moves:
        A list of tuples containing all possible positions this piece could
        move to.
    """
    position: tuple
    allowed_moves: List[tuple]
    name: str
    player: str

    def __init__(self, start: tuple, name: str, player: str) -> None:
        """Initialize a piece at given start location."""
        self.position = start
        self.allowed_moves = []
        self.name = name
        self.player = player

    def get_allowed_moves(self) -> List[tuple]:
        raise NotImplementedError


class Pawn(Piece):
    """A pawn can move one space forward, or two if it has not moved yet.
    It can capture by moving one space forward diagonally.

    === Attributes ===
    has_moved:
        Boolean which tracks whether or not this piece has moved yet.
    """
    has_moved: bool
    allowed_captures: List[tuple]

    def __init__(self, start: tuple, name: str, player: str) -> None:
        Piece.__init__(self, start, name, player)
        self.has_moved = False

    def get_allowed_captures(self) -> List[tuple]:
        # noinspection PyListCreation
        moves = []
        if self.player == 'black':
            moves.append((self.position[0] - 1, self.position[1] + 1))
            moves.append((self.position[0] - 1, self.position[1] - 1))

        if self.player == 'white':
            moves.append((self.position[0] + 1, self.position[1] + 1))
            moves.append((self.position[0] + 1, self.position[1] - 1))

        return moves

    def get_allowed_moves(self) -> List[tuple]:
        # noinspection PyListCreation
        moves = []
        if self.player == 'black':
            moves.append((self.position[0] - 1, self.position[1]))
            if self.has_moved is False:
                moves.append((self.position[0] - 2, self.position[1]))

        if self.player == 'white':
            moves.append((self.position[0] + 1, self.position[1]))
            if self.has_moved is False:
                moves.append((self.position[0] + 2, self.position[1]))

        return moves


class Rook(Piece):
    """A rook can move horizontally or vertically any number of spaces.

    === Attributes ===
    has_moved:
        Boolean which tracks whether or not this piece has moved yet.
    """
    has_moved: bool

    def get_allowed_moves(self) -> List[tuple]:
        # noinspection PyListCreation
        moves = []
        i = 1
        while i < 8:
            moves.append((self.position[0] + i, self.position[1]))
            moves.append((self.position[0] - i, self.position[1]))
            moves.append((self.position[0], self.position[1] + i))
            moves.append((self.position[0], self.position[1] - i))
            i += 1
        return moves


class Knight(Piece):
    """A knight can move to a position that is two spaces away in one dimension
    and one space away in the other."""

    def get_allowed_moves(self) -> List[tuple]:
        # noinspection PyListCreation
        moves = []
        moves.append((self.position[0] + 2, self.position[1] + 1))
        moves.append((self.position[0] + 2, self.position[1] - 1))
        moves.append((self.position[0] - 2, self.position[1] + 1))
        moves.append((self.position[0] - 2, self.position[1] - 1))
        moves.append((self.position[0] + 1, self.position[1] + 2))
        moves.append((self.position[0] - 1, self.position[1] + 2))
        moves.append((self.position[0] + 1, self.position[1] - 2))
        moves.append((self.position[0] - 1, self.position[1] - 2))

        return moves


class Bishop(Piece):
    """A bishop can move any number of spaces diagonally."""

    def get_allowed_moves(self) -> List[tuple]:
        # noinspection PyListCreation
        moves = []
        i = 1
        while i < 8:
            moves.append((self.position[0] + i, self.position[1] + i))
            moves.append((self.position[0] + i, self.position[1] - i))
            moves.append((self.position[0] - i, self.position[1] + i))
            moves.append((self.position[0] - i, self.position[1] - i))
            i += 1
        return moves


class Queen(Piece):
    """A queen can move any number of spaces vertically, horizontally, or
    diagonally."""

    def get_allowed_moves(self) -> List[tuple]:
        # noinspection PyListCreation
        moves = []
        i = 1
        while i < 8:
            moves.append((self.position[0] + i, self.position[1]))
            moves.append((self.position[0] - i, self.position[1]))
            moves.append((self.position[0], self.position[1] + i))
            moves.append((self.position[0], self.position[1] - i))
            moves.append((self.position[0] + i, self.position[1] + i))
            moves.append((self.position[0] + i, self.position[1] - i))
            moves.append((self.position[0] - i, self.position[1] + i))
            moves.append((self.position[0] - i, self.position[1] - i))
            i += 1
        return moves


class King(Piece):
    """A king can move one space at a time vertically, horizontally, or
    diagonally

    === Attributes ===
    has_moved:
        Boolean which tracks whether or not this piece has moved yet.
    """
    has_moved: bool

    def get_allowed_moves(self) -> List[tuple]:
        # noinspection PyListCreation
        moves = []
        moves.append((self.position[0], self.position[1] + 1))
        moves.append((self.position[0], self.position[1] - 1))
        moves.append((self.position[0] + 1, self.position[1]))
        moves.append((self.position[0] - 1, self.position[1]))
        moves.append((self.position[0] + 1, self.position[1] + 1))
        moves.append((self.position[0] + 1, self.position[1] - 1))
        moves.append((self.position[0] - 1, self.position[1] + 1))
        moves.append((self.position[0] - 1, self.position[1] - 1))
        return moves


class Nil(Piece):
    """A piece class for an empty square."""

    def get_allowed_moves(self) -> List[tuple]:
        return []


class Player:
    """An object representing a player in a game.

    === Attributes ===
    name:
        Either 'white' or 'black'.
    pieces:
        A list containing all the pieces that belong to this player.
    """
    name: str
    pieces: List[Piece]

    def __init__(self, name: str) -> None:
        self.name = name
        self.pieces = []


class GameBoard:
    """A game board for playing chess.

    === Attributes ===
    board:
        A list of lists creating an array, representing the squares of the game
        board and the pieces on each square at a given time.
    pieces:
        A list of all the pieces in the game.
    turn:
        The turn number. White moves on odd turns and black moves on even turns.
    players:
        A list of the players in the game.
    """
    board: List[List[Piece]]
    pieces: List[Piece]
    turn: int
    players: List[Player]
    promos: int

    def __init__(self) -> None:
        self.pieces = []
        self.board = []
        self.players = [Player('white'), Player('black')]
        # Initially fill an 8x8 board with Nil pieces (so all indices exist
        # properly)
        for i in range(8):
            self.board.append([])
            for j in range(8):
                self.board[i].append(Nil((i, j), '___', 'nil'))

        # Instantiate all the appropriate pieces to self.pieces, they will be
        # positioned appropriately every time the board updates.
        for i in range(8):
            self.pieces.append(Pawn((1, i), 'wp' + str(i + 1), 'white'))
            self.pieces.append(Nil((2, i), '___', 'nil'))
            self.pieces.append(Nil((3, i), '___', 'nil'))
            self.pieces.append(Nil((4, i), '___', 'nil'))
            self.pieces.append(Nil((5, i), '___', 'nil'))
            self.pieces.append(Pawn((6, i), 'bp' + str(i + 1), 'black'))
        self.pieces.append(Rook((0, 0), 'wr1', 'white'))
        self.pieces.append(Knight((0, 1), 'wk1', 'white'))
        self.pieces.append(Bishop((0, 2), 'wb1', 'white'))
        self.pieces.append(Queen((0, 3), 'wQu', 'white'))
        self.pieces.append(King((0, 4), 'wK*', 'white'))
        self.pieces.append(Bishop((0, 5), 'wb2', 'white'))
        self.pieces.append(Knight((0, 6), 'wk2', 'white'))
        self.pieces.append(Rook((0, 7), 'wr2', 'white'))

        self.pieces.append(Rook((7, 0), 'br1', 'black'))
        self.pieces.append(Knight((7, 1), 'bk1', 'black'))
        self.pieces.append(Bishop((7, 2), 'bb1', 'black'))
        self.pieces.append(King((7, 3), 'bK*', 'black'))
        self.pieces.append(Queen((7, 4), 'bQu', 'black'))
        self.pieces.append(Bishop((7, 5), 'bb2', 'black'))
        self.pieces.append(Knight((7, 6), 'bk2', 'black'))
        self.pieces.append(Rook((7, 7), 'br2', 'black'))

        self.turn = 1
        self.promos = 0

    def promote_pawn(self, pawn: Pawn) -> None:
        """Promote a pawn to another piece if it has reached the opposite end
        of the board"""
        self.pieces.remove(pawn)
        while True:
            promo_unit = input("What would you like to promote this pawn to, \n"
                               "a 'queen', 'rook', 'bishop', or 'knight' ?")
            if promo_unit not in ['queen', 'rook', 'bishop', 'knight']:
                print("Invalid promotion.")
                continue
            break
        if promo_unit == 'queen':
            self.pieces.append(Queen((pawn.position[0], pawn.position[1]),
                                     pawn.player[0] + 'Q' +
                                     str(1 + self.promos), pawn.player))
        if promo_unit == 'rook':
            self.pieces.append(Rook((pawn.position[0], pawn.position[1]),
                                    pawn.player[0] + 'r' +
                                    str(3 + self.promos), pawn.player))
        if promo_unit == 'bishop':
            self.pieces.append(Bishop((pawn.position[0], pawn.position[1]),
                                      pawn.player[0] + 'b' +
                                      str(3 + self.promos), pawn.player))
        if promo_unit == 'knight':
            self.pieces.append(Knight((pawn.position[0], pawn.position[1]),
                                      pawn.player[0] + 'k' +
                                      str(3 + self.promos), pawn.player))

    def update_board(self) -> None:
        """Update the board with the new positions of pieces."""
        # Update each players list of pieces
        for player in self.players:
            player.pieces.clear()
            for piece in self.pieces:
                if piece.player == player.name:
                    player.pieces.append(piece)

        # Create the printed board with updated positions of all pieces.
        for piece in self.pieces:
            row = piece.position[0]
            col = piece.position[1]
            self.board[row][col] = piece
        for row in self.board:
            print_row = ''
            for pos in row:
                print_row += ' ' + pos.name + ' '
            print(print_row)

    def move_piece(self, piece: Piece) -> bool:
        """Move a piece from one position to another. Returns true/false
        based on whether or not that piece has successfully been moved."""
        piece.allowed_moves = piece.get_allowed_moves()

        # Since pawns can capture and move in different ways, deal with this
        if isinstance(piece, Pawn):
            piece.allowed_captures = piece.get_allowed_captures()

            # Ensure the pawn can't capture directly ahead
            removals = []
            for move in piece.allowed_moves:
                target = self.board[move[0]][move[1]]
                if target.player != 'nil':
                    removals.append(move)
            for move in removals:
                piece.allowed_moves.remove(move)

            removals = []
            for move in piece.allowed_captures:
                # Get rid of all captures that would be off the board
                if move[0] > 7 or move[0] < 0 or move[1] > 7 or move[1] < 0:
                    removals.append(move)

            for move in removals:
                piece.allowed_captures.remove(move)

            # Ensure the pawn CAN capture diagonally, but only if there is a
            # piece to capture
            removals = []
            for move in piece.allowed_captures:
                target = self.board[move[0]][move[1]]
                if target.player == piece.player or target.player == 'nil':
                    removals.append(move)

            for move in removals:
                piece.allowed_captures.remove(move)
            piece.allowed_moves = piece.allowed_moves + piece.allowed_captures

        blocked_moves = []
        removals = []
        for move in piece.allowed_moves:
            # Get rid of all moves that would be off the board
            if move[0] > 7 or move[0] < 0 or move[1] > 7 or move[1] < 0:
                blocked_moves.append(move)
            else:
                target = self.board[move[0]][move[1]]
                # Get rid of all moves occupied by your pieces
                if target.player == piece.player:
                    removals.append(move)
                    blocked_moves.append(move)
                elif target.player != 'nil':
                    removals.append(move)

        # Get rid of all moves that are blocked by another piece, either yours
        # or your opponent's
        for move in removals:
            if move[0] > piece.position[0] and move[1] == piece.position[1]:
                for next_move in piece.allowed_moves:
                    if next_move[0] > move[0] and next_move[1] == move[1]:
                        blocked_moves.append(next_move)
            if move[0] > piece.position[0] and move[1] < piece.position[1]:
                for next_move in piece.allowed_moves:
                    if next_move[0] > move[0] and next_move[1] < move[1]:
                        blocked_moves.append(next_move)
            if move[0] > piece.position[0] and move[1] > piece.position[1]:
                for next_move in piece.allowed_moves:
                    if next_move[0] > move[0] and next_move[1] > move[1]:
                        blocked_moves.append(next_move)
            if move[0] < piece.position[0] and move[1] == piece.position[1]:
                for next_move in piece.allowed_moves:
                    if next_move[0] < move[0] and next_move[1] == move[1]:
                        blocked_moves.append(next_move)
            if move[0] < piece.position[0] and move[1] < piece.position[1]:
                for next_move in piece.allowed_moves:
                    if next_move[0] < move[0] and next_move[1] < move[1]:
                        blocked_moves.append(next_move)
            if move[0] < piece.position[0] and move[1] > piece.position[1]:
                for next_move in piece.allowed_moves:
                    if next_move[0] < move[0] and next_move[1] > move[1]:
                        blocked_moves.append(next_move)
            if move[0] == piece.position[0] and move[1] > piece.position[1]:
                for next_move in piece.allowed_moves:
                    if next_move[0] == move[0] and next_move[1] > move[1]:
                        blocked_moves.append(next_move)
            if move[0] == piece.position[0] and move[1] < piece.position[1]:
                for next_move in piece.allowed_moves:
                    if next_move[0] == move[0] and next_move[1] < move[1]:
                        blocked_moves.append(next_move)

        # Removes any duplicates from the list of blocked moves
        blocked_moves = list(dict.fromkeys(blocked_moves))

        # Remove all blocked moves from possible moves
        for move in blocked_moves:
            piece.allowed_moves.remove(move)

        if not piece.allowed_moves:
            print("No possible moves.")
            return False

        print("Possible moves: " + str(piece.allowed_moves))

        if isinstance(piece, Pawn) or isinstance(piece, King) or \
                isinstance(piece, Rook):
            piece.has_moved = True

        while True:
            stop = (int(input("What row would you like to move " +
                              piece.name + " to ?")),
                    int(input("What column would you like to move " +
                              piece.name + " to ?")))

            if not isinstance(stop, tuple):
                print("Invalid format.")
                continue

            count = 0
            for value in stop:
                if not isinstance(value, int):
                    print("Invalid format.")
                    continue
                count += 1

            if count != 2:
                print("Invalid format.")
                continue

            if stop not in piece.allowed_moves:
                print("That is not a valid move.")
                continue

            target = self.board[stop[0]][stop[1]]
            if target.player == piece.player:
                print("That is not a valid move.")
                continue

            if target.player == 'nil':
                target.position = piece.position
                piece.position = stop
            else:
                self.pieces.remove(target)
                self.pieces.append(Nil((piece.position[0], piece.position[1]),
                                       '___', 'nil'))
                piece.position = stop

            if isinstance(piece, Pawn) and (piece.position[0] == 0 or
                                            piece.position[0] == 7):
                self.promote_pawn(piece)

            self.update_board()
            self.turn += 1
            return True

    def get_piece(self) -> Piece:
        while True:
            if self.turn % 2 == 1:
                player = 'white'
                piece_name = str(input("White, which piece would you" +
                                       " like to move?"))
            else:
                player = 'black'
                piece_name = str(input("Black, which piece would you" +
                                       " like to move?"))
            for piece in self.pieces:
                if piece.name == piece_name and piece.player == player:
                    return piece
            print("Invalid piece.")
            continue

    def kings_alive(self) -> bool:
        """Check whether both players still have their King."""

        for player in self.players:
            has_king = False
            for piece in player.pieces:
                if isinstance(piece, King):
                    has_king = True
            if not has_king:
                print(player.name.capitalize() + " has lost their King!")
                return False
        return True


def play_chess() -> None:
    """Play a game of chess."""

    chess_board = GameBoard()
    chess_board.update_board()

    while chess_board.kings_alive():
        chess_board.move_piece(chess_board.get_piece())


play_chess()
