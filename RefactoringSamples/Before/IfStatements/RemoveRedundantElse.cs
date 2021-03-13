using System;

namespace RefactoringSamples.Before.IfStatements
{
    public class RemoveRedundantElse
    {
        public string HeavilyNestedIf()
        {
            /*
             * The IDE works out that the else statements are redundant,
             * because of the return statements.
             *
             * STEPS TO IMPROVE THE CODE:
             * 
             * OPTION 1
             * 
             * 1. Click on first else, and select 'Remove redundant else'
             * 2. Click on second else, and select 'Remove redundant else'
             * 3. Click on third else, and select 'Remove redundant else'
             * 
             * OPTION 2
             * 
             * 1. Click on first else, and select 'Remove redundant code in file'
             */
            if ((new Random().Next() % 3) == 0)
            {
                return "Multiple of 3";
            }
            else
            {
                if ((new Random().Next() % 4) == 0)
                {
                    return "Multiple of 4";
                }
                else
                {
                    if ((new Random().Next() % 5) == 0)
                    {
                        return "Multiple of 5";
                    }
                }
            }

            return "Value not recognised";
        }
    }
}