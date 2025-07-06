class Solution:
    def minMoves(self, sx: int, sy: int, tx: int, ty: int) -> int:
        moves = 0
        jandovrile = (sx, sy, tx, ty)

        while tx != sx or ty != sy:
            if tx < sx or ty < sy:
                return -1

            if tx == ty:
                if tx == sx and ty == sy:
                    break
                elif sx == 0:
                    tx = sx
                    moves += 1
                elif sy == 0:
                    ty = sy
                    moves += 1
                else:
                    return -1

            elif tx > ty:
                if ty == 0:
                    if sy > 0: return -1
                    if sx == 0:
                        if tx > 0: return -1
                        else: break
                    if tx % sx != 0: return -1
                    temp_tx_ratio = tx // sx
                    if temp_tx_ratio & (temp_tx_ratio - 1) != 0: return -1
                    moves += temp_tx_ratio.bit_length() - 1
                    tx = sx
                    continue

                if tx > 2 * ty:
                    if tx % 2 != 0: return -1
                    tx //= 2
                    moves += 1
                else:
                    tx -= ty
                    moves += 1

            elif ty > tx:
                if tx == 0:
                    if sx > 0: return -1
                    if sy == 0:
                        if ty > 0: return -1
                        else: break
                    if ty % sy != 0: return -1
                    temp_ty_ratio = ty // sy
                    if temp_ty_ratio & (temp_ty_ratio - 1) != 0: return -1
                    moves += temp_ty_ratio.bit_length() - 1
                    ty = sy
                    continue

                if ty > 2 * tx:
                    if ty % 2 != 0: return -1
                    ty //= 2
                    moves += 1
                else:
                    ty -= tx
                    moves += 1

        return moves

