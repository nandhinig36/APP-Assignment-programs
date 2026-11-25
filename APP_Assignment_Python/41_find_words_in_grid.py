def find_words(board, words):
    rows, cols = len(board), len(board[0])
    found = set()
    def search(r,c,node,path):
        ch = board[r][c]
        if ch not in node: return
        nxt = node[ch]
        word = nxt.pop("$", None)
        if word: found.add(word)
        board[r][c] = "#"
        for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
            nr,nc = r+dr,c+dc
            if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#":
                search(nr,nc,nxt,path+ch)
        board[r][c] = ch
    trie = {}
    for word in words:
        node = trie
        for ch in word: node = node.setdefault(ch,{})
        node["$"] = word
    for r in range(rows):
        for c in range(cols): search(r,c,trie,"")
    return sorted(found)

if __name__ == "__main__":
    grid = [list(x) for x in ["oath","eeta","ihkr","iflv"]]
    print(find_words(grid, ["oath","pea","eat","rain"]))
