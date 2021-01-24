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

import Chessboard

# Assignation de variable à l'instance ChessBoard
chessboard = Chessboard.Chessboard()

if __name__ == '__main__':
    # Variable de partie (Game = Partie en cours / Color = Couleur de démarrage)
    game = True
    color = True
    # Tant que la partie est en cours
    while game:
        # Imprimer l'échiquier
        print(chessboard.print_chess(0))
        if chessboard.is_chess_mate() is not None:
            print("AVERTISSEMENT: Un Roi est en échec, vous devez contrer cet échec.")
        # Demander quelle pièce le joueur souhaite t'il déplacer ?
        case = input(
            "Au tour des pièces " + ("blancs" if color else "noirs") + ": Quel pièce souhaitez-vous déplacer ?")
        # Récupère l'instance de pièce (si elle existe) à partir du dictionnaire de l'échiquier
        pawn = chessboard.get_specified_piece(case)
        # Vérifie qu'on a selectionné une pièce
        if pawn != 0 and pawn != -1:
            # Vérifie que la pièce peut bouger
            if len(pawn.moves) == 0:
                print("Vous avez sélectionné une pièce ne pouvant pas bouger. Merci d'en selectionner un autre.")
                continue
            # Vérifie que la pièce est de la même couleur que le joueur
            if pawn.color != color:
                print("Vous avez sélectionné une pièce ne vous appartenant pas. Merci d'en selectionner un autre.")
                continue
            else:
                # Affiche les possibilités de déplacements
                print(chessboard.print_chess(pawn))
                movingCase = input(
                    "Vous avez sélectionné un(e) " + pawn.type + ". Ou souhaitez-vous le déplacer ? (" + str(
                        pawn.moves) + ")")
                # Vérifie que le déplacement est possible
                if chessboard.move_piece(case, movingCase):
                    color = not color
                    print("Coup accepté. ✅")
                else:
                    print("Coup impossible. ❌")
        else:
            print("Vous n'avez pas sélectionné de pièce. Merci de réessayer.")
