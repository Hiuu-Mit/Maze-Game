from maze import create_maze
import pygame

def main():
    row = 9
    col = 9
    maze = create_maze(row, col)

    for row in maze:
        print(row)
        

   
if __name__ == "__main__":
    main()