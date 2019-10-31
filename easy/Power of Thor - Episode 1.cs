using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Collections;
using System.Collections.Generic;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 * ---
 * Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.
 **/
class Player
{
    static void Main(string[] args)
    {
        string[] inputs = Console.ReadLine().Split(' ');
        int lightX = int.Parse(inputs[0]); // the X position of the light of power
        int lightY = int.Parse(inputs[1]); // the Y position of the light of power
        int initialTx = int.Parse(inputs[2]); // Thor's starting X position
        int initialTy = int.Parse(inputs[3]); // Thor's starting Y position

        // game loop
        while (true)
        {
            int remainingTurns = int.Parse(Console.ReadLine()); // The remaining amount of turns Thor can move. Do not remove this line.
            StringBuilder instruction = new StringBuilder();
            if(initialTy > lightY) 
            {
                instruction.Append('N');
                initialTy--;
            } 
            else if(initialTy < lightY)
            {
                instruction.Append('S');
                initialTy++;
            }

            if(initialTx > lightX)
            {
                instruction.Append('W');
                initialTx--;
            }
            else if(initialTx < lightX) 
            {
                instruction.Append('E');
                initialTx++;
            }
            Console.WriteLine(instruction.ToString());
        }
    }
}