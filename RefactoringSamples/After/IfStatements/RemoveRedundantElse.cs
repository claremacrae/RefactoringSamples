using System;

namespace RefactoringSamples.After.IfStatements
{
    // begin-snippet: RemoveRedundantElse-After
    public class RemoveRedundantElse
    {
        public string HeavilyNestedIf()
        {
            if ((new Random().Next() % 3) == 0)
            {
                return "Multiple of 3";
            }

            if ((new Random().Next() % 4) == 0)
            {
                return "Multiple of 4";
            }

            if ((new Random().Next() % 5) == 0)
            {
                return "Multiple of 5";
            }

            return "Value not recognised";
        }
    }
    // end-snippet
}