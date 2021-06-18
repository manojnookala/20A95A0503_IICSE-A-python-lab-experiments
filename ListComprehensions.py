if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    output = [];
    abc = [];
    for X in range(x+1):
        for Y in range(y+1):
            for Z in range(z+1):
                if X+Y+Z != n:
                    abc = [X,Y,Z];
                    output.append(abc);
print(output);
OUTPUT:
  [[0, 0, 0]
   [0, 0, 1]
   [0, 1, 0]
   [0, 1, 2]
   [0, 2, 1]
   [0, 2, 2]
   [1, 0, 0]
   [1, 0, 2]
   [1, 1, 1]
   [1, 1, 2]
   [1, 2, 0]
   [1, 2, 1]
   [1, 2, 2]
   [2, 0, 1]
   [2, 0, 2]
   [2, 1, 0]
   [2, 1, 1]
   [2, 1, 2]
   [2, 2, 0]
   [2, 2, 1]
   [2, 2, 2]]
