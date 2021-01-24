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

from pawns import Piece
from pawns.BishopPiece import BishopPiece
from pawns.KingPiece import KingPiece
from pawns.KnightPiece import KnightPiece
from pawns.PawnPiece import PawnPiece
from pawns.QueenPiece import QueenPiece
from pawns.RookPiece import RookPiece


class Chessboard:
    # On définit les coordonnées verticales possibles
    alpha = ["a", "b", "c", "d", "e", "f", "g", "h"]

    # Initialise l'instance de la classe Chessboard
    def __init__(self):
        self.ech = \
            {"a8": RookPiece("a8", True), "b8": KnightPiece("b8", True), "c8": BishopPiece("c8", True),
             "d8": KingPiece("d8", True), "e8": QueenPiece("e8", True), "f8": BishopPiece("f8", True),
             "g8": KnightPiece("g8", True), "h8": RookPiece("h8", True),
             "a7": PawnPiece("a7", True), "b7": PawnPiece("b7", True), "c7": PawnPiece("c7", True),
             "d7": PawnPiece("d7", True), "e7": PawnPiece("e7", True), "f7": PawnPiece("f7", True),
             "g7": PawnPiece("g7", True), "h7": PawnPiece("h7", True),
             "a6": 0, "b6": 0, "c6": 0, "d6": 0, "e6": 0, "f6": 0, "g6": 0, "h6": 0,
             "a5": 0, "b5": 0, "c5": 0, "d5": 0, "e5": 0, "f5": 0, "g5": 0, "h5": 0,
             "a4": 0, "b4": 0, "c4": 0, "d4": 0, "e4": 0, "f4": 0, "g4": 0, "h4": 0,
             "a3": 0, "b3": 0, "c3": 0, "d3": 0, "e3": 0, "f3": 0, "g3": 0, "h3": 0,
             "a2": PawnPiece("a2", False), "b2": PawnPiece("b2", False), "c2": PawnPiece("c2", False),
             "d2": PawnPiece("d2", False), "e2": PawnPiece("e2", False), "f2": PawnPiece("f2", False),
             "g2": PawnPiece("g2", False), "h2": PawnPiece("h2", False),
             "a1": RookPiece("a1", False), "b1": KnightPiece("b1", False), "c1": BishopPiece("c1", False),
             "d1": KingPiece("d1", False), "e1": QueenPiece("e1", False), "f1": BishopPiece("f1", False),
             "g1": KnightPiece("g1", False), "h1": RookPiece("h1", False)}

        # On définit un tableau contenant les instances des Rois
        self.kings = [self.ech["d8"], self.ech["d1"]]

        self.update_all_pieces()

    """
        Prend en paramètre soit une valeur 0, soit une instance de Piece.
        Retourne une chaîne de caractère correspondant à un échiquier, à imprimer dans la console.
    """

    def print_chess(self, pawn):
        chessStr = "  | ".rjust(5)
        i = 0
        while i < len(self.alpha):
            chessStr += (str(self.alpha[i]) + " ").rjust(5)
            i += 1
        chessStr += "\n--------------------------------------------------\n"

        i = 0
        rowcount = 8
        info = ""

        while i < len(self.ech):
            chessStr += (str(rowcount) + " | ").rjust(5)

            rowcount -= 1

            y = 0
            while y < 8:
                if self.ech[self.alpha[y] + str(rowcount + 1)] == 0:
                    if pawn == 0:
                        chessStr += ". ".rjust(5)
                    elif self.alpha[y] + str(rowcount + 1) in pawn.moves:
                        if self.ech[self.alpha[y] + str(rowcount + 1)] in Piece.enPassant:
                            chessStr += "X* ".rjust(5)
                            info = "* : Vous pouvez éliminer la pièce qui est passée avec un pion (En-Passant)"
                        else:
                            chessStr += "x ".rjust(5)
                    else:
                        chessStr += ". ".rjust(5)
                else:
                    if pawn != 0 and (self.alpha[y] + str(rowcount + 1)) in pawn.moves:
                        chessStr += (self.ech[self.alpha[y] + str(rowcount + 1)].symbol + "<").rjust(5)
                    else:
                        chessStr += (self.ech[self.alpha[y] + str(rowcount + 1)].symbol + " ").rjust(5)
                y += 1
                i += 1
            chessStr += "\n"

        if info != "":
            chessStr += "Information: " + info

        return chessStr

    """
        Prend en paramètre une case de l'échiquier.
        Retourne l'instance d'une pièce, correspondant à la position donnée en paramètre.
        Ou, le cas échéant, retourne 0 s'il n'y a pas de pièce, -1 si la position n'existe pas.
    """

    def get_specified_piece(self, case):
        if case in self.ech.keys():
            return self.ech[case]
        elif case[0] in self.alpha and 0 < int(case[1]) < 9:
            return 0
        else:
            return -1

    """
        Mets à jour les déplacements possibles de toutes les pièces.
        Ne prend aucun paramètre et ne retourne aucune valeur.
    """

    def update_all_pieces(self):
        i = 0
        liste = list(self.ech.values())
        while i < len(self.ech):
            if liste[i] != 0:
                liste[i].update_moves(self)
            i += 1

    """
        Prend en paramètre une case de l'échiquier, ainsi que la case de destination souhaitée.
        Retourne True si le déplacement a été effectué, ou False si le déplacement n'est pas possible.
    """

    def move_piece(self, case, movingcase):
        piece = self.get_specified_piece(case)
        # Vérifie si le mouvement est dans les possibilités de déplacement de la pièce
        if movingcase in piece.moves:
            # Déplacer la pièce
            temp = self.ech[movingcase]
            self.ech[movingcase] = piece
            piece.setposition(movingcase)
            # On supprime l'ancienne postion de la pièce
            self.ech[case] = 0
            # On met à jour le déplacement de toutes les pièces
            self.update_all_pieces()

            # On vérifie si ce mouvement met en échec le Roi
            kingColor = self.is_chess_mate()
            if kingColor == piece.color:
                print("Ce déplacement mettra en échec votre Roi, vous ne pouvez donc pas effectuer celui-ci.")
                # On rétablit l'échiquier comme avant les déplacements
                self.ech[movingcase] = temp
                piece.setposition(case)
                self.ech[case] = piece
                self.update_all_pieces()
                return False

            # Vérifie si on peut faire une prise en passant, et si oui elle disparaît de l'échiquier
            if piece.type == "Pion" and movingcase in Piece.enPassant:
                self.ech[Piece.enPassant[movingcase].position] = 0
            # On remet à zéro le dictionnaire EnPassant
            Piece.enPassant = {}
            # Si la pièce fait un mouvement de deux cases, on l'ajoute dans le dictionnaire EnPassant
            if piece.type == "Pion" and abs(int(movingcase[1]) - int(case[1])) == 2:
                Piece.enPassant[
                    movingcase[0] + str(int(movingcase[1]) + 1 if piece.color else int(movingcase[1]) - 1)] = piece

            # On vérifie si la pièce est éligible à une promotion
            if piece.type == "Pion" and (piece.position[1] == "1" or piece.position[1] == "8"):
                while True:
                    pieceName = input(
                        "En quelle pièce souhaitez-vous que le Pion soit promu ? (Dame/Tour/Fou/Cavalier)")
                    if pieceName == "Dame":
                        self.ech[movingcase] = QueenPiece(movingcase, piece.color)
                        break
                    elif pieceName == "Tour":
                        self.ech[movingcase] = RookPiece(movingcase, piece.color)
                        break
                    elif pieceName == "Fou":
                        self.ech[movingcase] = BishopPiece(movingcase, piece.color)
                        break
                    elif pieceName == "Cavalier":
                        self.ech[movingcase] = KnightPiece(movingcase, piece.color)
                        break

            # On supprime de la mémoire l'ancien pion, qui n'est plus sur l'échiquier
            del temp

            return True
        else:
            return False

    """
        Ne prend pas de paramètre.
        Retourne la couleur du Roi en échec s'il l'est, ou None s'il ne l'est pas.
    """

    def is_chess_mate(self):
        kings = self.get_kings()
        i = 0
        liste = list(self.ech.values())
        while i < len(self.ech):
            if liste[i] != 0:
                for y in range(0, len(kings)):
                    if kings[y].color != liste[i].color and kings[y].position in liste[i].moves:
                        return kings[y].color
            i += 1
        return None

    def get_kings(self):
        return self.kings

    """
        Retourne les coordonnées verticales possibles, contenues dans la variable alpha.
    """

    def getalpha(self):
        return self.alpha
