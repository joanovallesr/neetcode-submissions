class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # 1. Build a lightweight Trie using nested dictionaries
        root = {}
        for word in words:
            current = root
            for char in word:
                if char not in current:
                    current[char] = {}
                current = current[char]
            # Store the absolute word at the end node instead of a boolean flag.
            # This completely avoids tracking an active 'path' array during DFS.
            current["$"] = word
            
        rows, cols = len(board), len(board[0])
        result = []
        
        # Directions array for scannable neighbor verification
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # 2. Define the Recursive DFS Backtracking helper
        def dfs(r: int, c: int, parent_node: dict):
            char = board[r][c]
            current_node = parent_node[char]
            
            # Check if a complete word is formed at this node
            matched_word = current_node.pop("$", None)
            if matched_word:
                result.append(matched_word)
                # Optimization Note: We pop the word from the Trie here 
                # so we never find or add it a second time from another path!
            
            # Mark the current grid cell as visited
            board[r][c] = '#'
            
            # Explore all 4 neighboring directions
            for dr, dc in directions:
                next_r, next_c = r + dr, c + dc
                
                # Boundary check + pruning validation
                if 0 <= next_r < rows and 0 <= next_c < cols:
                    next_char = board[next_r][next_c]
                    if next_char in current_node:
                        dfs(next_r, next_c, current_node)
                        
            # Backtrack: Restore the cell's original character before exiting the frame
            board[r][c] = char
            
            # High-Level Optimization: Prune childless branches from the Trie dynamically.
            # If a dictionary character path becomes entirely empty, we completely delete 
            # it from its parent node. This shrinks the search space down to zero over time.
            if not current_node:
                parent_node.pop(char)

        # 3. Outer Traversal: Run DFS from every single cell matching a Trie root starter letter
        for r in range(rows):
            for c in range(cols):
                if board[r][c] in root:
                    dfs(r, c, root)
                    
        return result