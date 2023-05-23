# LaTeX

Overleaf has a lot of great quick tutorials for different LaTeX functionalities that go into writing a paper:
 * __Tables__: https://www.overleaf.com/learn/latex/Tables
    * __Fancy Tables__: using the `booktabs` package is nice; can't find a good tutorial though.
    * __Pandas Hack__: If you create a pandas dataframe, you can turn it to a latex table using `df.to_latex()`. This will return a string that you can copy into a tex file. You can even specify how many digits you want to show. For example,
         * `df.to_latex(float_format="%.2f")` will format floats with two digits past the decimal like this: `0.01`
         * `df.to_latex(float_format="%.2e")` will format floats in scientific notation with two digits past the decimal like this: `1.00e-02`
         * Documentation: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_latex.html
         * Example: https://github.com/suzannastep/linearlayers/blob/main/teacher_networks_plotting_results.ipynb cell 28 (edited) 
 * __Figures__: https://www.overleaf.com/learn/latex/Inserting_Images
    * __Sub-Figures__: https://www.overleaf.com/learn/latex/How_to_Write_a_Thesis_in_LaTeX_(Part_3)%3A_Figures%2C_Subfigures_and_Tables#Subfigures
 * __Algorithm blocks__: https://www.overleaf.com/learn/latex/Algorithms
 * __Bibliographies__: https://www.overleaf.com/learn/how-to/Using_bibliographies_on_Overleaf
 * __Backup to Git__: You can backup important Overleaf files. This can be beneficial because sometimes Overleaf has had issues around submission deadlines. Here's how to set this up.
      1. From within a file, click on the menu icon in the top-left corner
      1. Click “Github” under “sync” and follow the prompts to connect with your GitHub account
      1. Return to the overleaf project. Go back to the menu and click on Github again
      1. From there, you’re given the option to create a new private or public Github repo for the file
      1. Optionally, you can add collaborators to the git repo from Github’s website
      1. Regularly (perhaps every day, after significant change, etc.), go back Menu -> GitHub and create a new commit for recent changes
