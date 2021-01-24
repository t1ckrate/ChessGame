enPassant = {}


#  MIT License
#
#  Copyright (c) 2021 Thomas PERROT / t1ckrate (https://github.com/t1ckrate).
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
#  The Software is provided “as is”, without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose and noninfringement. In no event shall the authors or copyright holders X be liable for any claim, damages or other liability, whether in an action of contract, tort or otherwise, arising from, out of or in connection with the software or the use or other dealings in the Software.
#  Except as contained in this notice, the name of copyright holder (Thomas PERROT) shall not be used in advertising or otherwise to promote the sale, use or other dealings in this Software without prior written authorization from the copyright holder (Thomas PERROT).
#

class Piece:
    """
       Object class for Piece
       Type = Piece type
       Position = Current position on the ChessBoard
       Moves = Table composed of where pieces can move
       Color = Piece color (Team)
       Symbol = UTF-8 Symbol
    """

    def __init__(self, type, position, moves, color, symbol):
        self.type = type
        self.moves = moves
        self.color = color
        self.symbol = symbol
        self.position = position

    def gettype(self):
        return self.type

    def getposition(self):
        return self.position

    def setposition(self, position):
        self.position = position

    def getmoves(self):
        return self.moves

    def setmoves(self, moves):
        self.moves = moves

    def getcolor(self):
        return self.color

    def getsymbol(self):
        return self.symbol

    def update_moves(self, chessboard):
        return

    """
        Prend en paramètre une instance d'échiquier (Chessboard).
        Retourne un tableau comportant les positions à laquelle une pièce peut se déplacer de manière diagonale.
    """

    def get_diagonal_moves(self, chessboard):
        vertical = chessboard.getalpha().index(self.getposition()[0])
        horizontal = int(self.getposition()[1])
        moves = []

        i = 0
        while vertical + i < 7 and horizontal + i < 7:
            i += 1
            position = chessboard.getalpha()[vertical + i] + str(horizontal + i)
            piece = chessboard.get_specified_piece(position)
            if piece == -1:
                break
            if (piece == 0) or (piece != 0 and self.color != piece.color):
                moves.append(position)
            if piece != 0:
                break

        i = 0
        while vertical - i > 0 and horizontal - i > 0:
            i += 1
            position = chessboard.getalpha()[vertical - i] + str(horizontal - i)
            piece = chessboard.get_specified_piece(position)
            if piece == -1:
                break
            if (piece == 0) or (piece != 0 and self.color != piece.color):
                moves.append(position)
            if piece != 0:
                break

        i = 0
        while vertical + i < 7 and horizontal - i > 0:
            i += 1
            position = chessboard.getalpha()[vertical + i] + str(horizontal - i)
            piece = chessboard.get_specified_piece(position)
            if piece == -1:
                break
            if (piece == 0) or (piece != 0 and self.color != piece.color):
                moves.append(position)
            if piece != 0:
                break

        i = 0
        while vertical - i > 0 and horizontal + i < 7:
            i += 1
            position = chessboard.getalpha()[vertical - i] + str(horizontal + i)
            piece = chessboard.get_specified_piece(position)
            if piece == -1:
                break
            if (piece == 0) or (piece != 0 and self.color != piece.color):
                moves.append(position)
            if piece != 0:
                break

        return moves

    """
        Prend en paramètre une instance d'échiquier (Chessboard).
        Retourne un tableau comportant les positions à laquelle une pièce peut se déplacer de manière verticale.
    """

    def get_vertical_moves(self, chessboard):
        vertical = chessboard.getalpha().index(self.getposition()[0])
        horizontal = int(self.getposition()[1])

        moves = []

        i = 0
        while horizontal - i > 0:
            i += 1
            position = chessboard.getalpha()[vertical] + str(horizontal - i)

            piece = chessboard.get_specified_piece(position)
            if piece == -1:
                break
            if (piece == 0) or (piece != 0 and self.color != piece.color):
                moves.append(position)
            if piece != 0:
                break

        i = 0
        while horizontal + i < 8:
            i += 1
            position = chessboard.getalpha()[vertical] + str(horizontal + i)

            piece = chessboard.get_specified_piece(position)
            if piece == -1:
                break
            if (piece == 0) or (piece != 0 and self.color != piece.color):
                moves.append(position)
            if piece != 0:
                break

        return moves

    """
        Prend en paramètre une instance d'échiquier (Chessboard).
        Retourne un tableau comportant les positions à laquelle une pièce peut se déplacer de manière horizontale.
    """

    def get_horizontal_moves(self, chessboard):
        vertical = chessboard.getalpha().index(self.getposition()[0])
        horizontal = int(self.getposition()[1])

        moves = []

        i = 0
        while vertical + i < 7:
            i += 1
            position = chessboard.getalpha()[vertical + i] + str(horizontal)

            piece = chessboard.get_specified_piece(position)
            if piece == -1:
                break
            if (piece == 0) or (piece != 0 and self.color != piece.color):
                moves.append(position)
            if piece != 0:
                break

        i = 0
        while vertical - i > 0:
            i += 1
            position = chessboard.getalpha()[vertical - i] + str(horizontal)

            piece = chessboard.get_specified_piece(position)

            if piece == -1:
                break
            if (piece == 0) or (piece != 0 and self.color != piece.color):
                moves.append(position)
            if piece != 0:
                break

        return moves

    """
        Prend en paramètre une instance d'échiquier (Chessboard).
        Retourne un tableau comportant les positions à laquelle un pion peut se déplacer.
    """

    def get_pawn_moves(self, chessboard):
        vertical = chessboard.getalpha().index(self.getposition()[0])
        horizontal = int(self.getposition()[1])

        moves = []
        if self.position[1] == "7" and self.color:
            moves.append(self.get_move(chessboard, vertical, horizontal - 2))
        elif self.position[1] == "2" and not self.color:
            moves.append(self.get_move(chessboard, vertical, horizontal + 2))

        moves.append(self.get_move(chessboard, vertical, horizontal - 1 if self.color else horizontal + 1))
        moves = self.moves_remove_none(moves)

        # Retire les pièces étant dans le champ du pion, car elles ne peuvent pas être mangées avec un déplacement
        # standard.
        finalmoves = []
        for i in range(0, len(moves)):
            location = moves[i]
            piece = chessboard.get_specified_piece(location)
            if piece == 0:
                finalmoves.append(location)

        moves = finalmoves
        moves.extend(self.get_diagonal_piece(chessboard))

        # Vérifie si un mouvement EnPassant est possible sur le côté droit
        right = self.get_move(chessboard, vertical - 1, horizontal)
        if right is not None:
            piece = chessboard.get_specified_piece(right)
            if piece != 0:
                if piece.type == "Pion" and piece.color != self.color and (
                        (self.color and self.position[1] == "4") or (not self.color and horizontal == 5)) \
                        and (right[0] + str(int(right[1]) + 1 if piece.color else int(right[1]) - 1)) in enPassant:
                    moves.append(right[0] + str(
                        int(right[1]) - 1 if self.color else int(right[1]) + 1))

        # Vérifie si un mouvement EnPassant est possible sur le côté gauche
        left = self.get_move(chessboard, vertical + 1, horizontal)
        if left is not None:
            piece = chessboard.get_specified_piece(left)
            if piece != 0:
                if piece.type == "Pion" and piece.color != self.color and ((self.color and self.position[1] == "4")
                                                                           or (not self.color and horizontal == 5)) \
                        and (left[0] + str(int(left[1]) + 1 if piece.color else int(left[1]) - 1)) in enPassant:
                    moves.append(left[0] + str(
                        int(left[1]) - 1 if self.color else int(left[1]) + 1))

        return self.moves_remove_none(moves)

    """
        Prend en paramètre une instance d'échiquier (Chessboard).
        Retourne un tableau comportant les positions à laquelle une pièce peut se déplacer en diagonale.
    """

    def get_diagonal_piece(self, chessboard):
        vertical = chessboard.getalpha().index(self.getposition()[0])
        horizontal = int(self.getposition()[1])

        moves = []

        if self.color:
            moves.append(self.get_move(chessboard, vertical - 1, horizontal - 1))
            moves.append(self.get_move(chessboard, vertical + 1, horizontal - 1))
        else:
            moves.append(self.get_move(chessboard, vertical + 1, horizontal + 1))
            moves.append(self.get_move(chessboard, vertical - 1, horizontal + 1))

        moves = self.moves_remove_none(moves)
        finalmoves = []
        for i in range(0, len(moves)):
            location = moves[i]
            piece = chessboard.get_specified_piece(location)
            if piece != 0 and piece.color != self.color:
                finalmoves.append(location)

        return finalmoves

    """
        Prend en paramètre une instance d'échiquier (Chessboard).
        Retourne un tableau comportant les positions à laquelle un cavalier peut se déplacer.
    """

    def get_knight_moves(self, chessboard):
        vertical = chessboard.getalpha().index(self.getposition()[0])
        horizontal = int(self.getposition()[1])
        moves = self.moves_remove_none([self.get_move(chessboard, vertical + 1, horizontal + 2),
                                        self.get_move(chessboard, vertical - 1, horizontal + 2),
                                        self.get_move(chessboard, vertical + 2, horizontal - 1),
                                        self.get_move(chessboard, vertical + 2, horizontal + 1),
                                        self.get_move(chessboard, vertical + 1, horizontal - 2),
                                        self.get_move(chessboard, vertical - 1, horizontal - 2)])

        finalmoves = []
        for i in range(0, len(moves)):
            piece = chessboard.get_specified_piece(moves[i])
            if piece and piece.color == self.color:
                continue

            finalmoves.append(moves[i])

        return finalmoves

    """
        Prend en paramètre une instance d'échiquier (Chessboard).
        Retourne un tableau comportant les positions à laquelle une pièce peut se déplacer autour de lui même.
    """

    def get_around_moves(self, chessboard):
        vertical = chessboard.getalpha().index(self.getposition()[0])
        horizontal = int(self.getposition()[1])
        moves = self.moves_remove_none([self.get_move(chessboard, vertical + 1, horizontal + 1),
                                        self.get_move(chessboard, vertical - 1, horizontal - 1),
                                        self.get_move(chessboard, vertical + 1, horizontal - 1),
                                        self.get_move(chessboard, vertical - 1, horizontal + 1),
                                        self.get_move(chessboard, vertical + 1, horizontal),
                                        self.get_move(chessboard, vertical - 1, horizontal),
                                        self.get_move(chessboard, vertical, horizontal + 1),
                                        self.get_move(chessboard, vertical, horizontal - 1)])

        finalmoves = []
        for i in range(0, len(moves)):
            piece = chessboard.get_specified_piece(moves[i])
            if piece and piece.color == self.color:
                continue

            finalmoves.append(moves[i])

        return finalmoves

    """
        Prend en paramètre une instance d'échiquier (Chessboard), un point de destination X et un point de destination Y.
        Retourne un position si le déplacement est possible, ou une valeur Nulle le cas échiant.
    """

    def get_move(self, chessboard, tox, toy):
        if 8 > tox >= 0 and 8 >= toy > 0:
            location = chessboard.getalpha()[tox] + str(toy)
            return location
        else:
            return None

    """
        Prend en paramètre un tableau de déplacements incluant des valeurs potentiellement nulles.
        Retourne un tableau de valeurs non-nulles.
    """

    def moves_remove_none(self, moves):
        finalMoves = []
        for i in range(0, len(moves)):
            if moves[i] is not None:
                finalMoves.append(moves[i])
        return finalMoves
