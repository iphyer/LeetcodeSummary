class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        
        def DFS(room):
            visited.add(room)
            for key in rooms[room]:
                if key not in visited:
                    DFS(key)
        DFS(0)
        return len(visited) == len(rooms)
