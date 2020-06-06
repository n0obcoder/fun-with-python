<h1>todo_list_maker</h1>

This is a simple todo_list_maker application that I have built in Python.

<h2>Adding a to-do list item ("--do" argument)</h2>
Running the todo_list_maker to add a new todo list item to the default todo list(.txt file) at the default location (Desktop)

```
python todo_list_maker.py --do "Learn Ableton Live 10"
```

<h2>Specifying the name of to-do list ("--name" argument)</h2>
Running the todo_list_maker to add a new todo list item to the specified todo list(todo_music.txt for this example) at the default location (Desktop)

```
python todo_list_maker.py --do "Learn Ableton Live 10" --name "todo_music"
```


<h2>Specifying the path of the to-do list ("--path" argument)</h2>
Running the todo_list_maker to add a new todo list item to the specified todo list(todo_music.txt for this example) at the specified location (C:/Users/anime/Documets/)

```
python todo_list_maker.py --do "Learn Ableton Live 10" --name "todo_music" --path "C:/Users/anime/Documets/"
```

<h2>Renewing a to-do list ("-n" argument)</h2>
Running the todo_list_maker to add a new todo list item by renewing the todo list(if it exists already)

```
python todo_list_maker.py --do "Learn Ableton Live 10" -n
```

<h2>Listing all the to-do list items ("-l" argument)</h2>
Listing (printing) down all the to-do list items of the to-do list on the command-line</h2>

```
python todo_list_maker.py -l
```
