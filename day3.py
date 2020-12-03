def FindTrees(x,y): 
    f = open("AOC_day3_input.txt")
    l1 = f.readline().rstrip()
    i = 0
    count =0
    while True:
        if y > 1:
            for _ in range(y-1):
                l3 = f.readline()
        l2 = f.readline().rstrip()
        if not l2: break  #EOF
        i =(i + x)% len(l2)
        if l2[i] == "#":
            count +=1
    f.close()
    return count

stepx = [1,3,5,7,1]
stepy = [1,1,1,1,2]
result =[]
mul = 1
for ele in range(len(stepx)):
    result += [FindTrees(stepx[ele],stepy[ele])]
    mul *= result[ele]

print(f"List of Tree counts is {result} \nThe Product is {mul}")

'''
THe question :

"These aren't the only trees, though; due to something you read about once involving arboreal genetics and biome stability, the same pattern repeats to the right many times(infinitely).
You start on the open square (.) in the top-left corner and need to reach the bottom (below the bottom-most row on your map).

The toboggan can only follow a few specific slopes (you opted for a cheaper model that prefers rational numbers); start by counting all the trees you would encounter for the slope right 3, down 1:

From your starting position at the top-left, check the position that is right 3 and down 1. Then, check the position that is right 3 and down 1 from there, and so on until you go past the bottom of the map.

The locations you'd check in the above example are marked here with O where there was an open square and X where there was a tree:
..##.........##.........##.........##.........##.........##.......  --->
#..O#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....X..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#O#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..X...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.X#.......#.##.......#.##.......#.##.......#.##.....  --->
.#.#.#....#.#.#.#.O..#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........X.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.X#...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...#X....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...X.#.#..#...#.#.#..#...#.#.#..#...#.#  ---> "
