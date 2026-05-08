# What Copilot generated
Copilot generated the following lines in src/data\_cleaning.py.
```
12. return pd.read_csv(file_path)
29. df.loc[:, 'qty'] = pd.to_numeric(df['qty'], errors='coerce')
30. df.loc[:, 'price'] = pd.to_numeric(df['price'], errors='coerce') 
31. df = df[(df['qty'] >= 0) & (df['price'] >= 0)]
39. def trim_whitespace(df):
40.         string_columns = df.select_dtypes(include=['object']).columns
41.         for col in string_columns:
42.                 df.loc[:, col] = df[col].str.rstrip()
43.                 df.loc[:, col] = df[col].str.lstrip()  # Added: Remove leading whitespace as well
44.         return df
```
where the numbers at the beginning of each line is the line number in the file.

# Which functions or code blocks came primarily from Copilot’s suggestions? How did you prompt it (comments, partial code, etc.)?
The two functions that carried a majority was `trim_whitespace(df)` and `load_data(file_path:str)`. I prompted Copilot by simply adding comments above the function declaration telling it what I wanted the function to do, and then it simply filled it out.

# What you modified
I modified line 42. and 43. as it gave back code that gave an error as it forgot to call .str after .rstrip(). I broke it up into two lines for clearer logic. I also changed wherever it mentions a column name as it struggled with the raw .csv or just couldn't see it. These were the only changes I really made to the project as everything else I coded myself which I just naturally debugged. Everything else Copilot gave worked first try and didn't crash. 

# What I learned
What i learned was that the best thing I can do is first outline the structure of my project (have functions that I know I will need in my project), and give some background information on what I want it to do, and if I get lost / want help I can use Copilot and adjust accordingly. The project would not have worked had I just given Copilot an idea, but because there was a clean file structure and functions it made it much easier. Another thing I learned not just about data cleaning but in general is to not reinvent the wheel. There are tools (like pandas) that will help you with what you need, and it's important to take advantage of libraries.
