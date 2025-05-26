# define a list of colors
colors = ["red","blue","green","yellow","orange","purple"]
#ask user for the order sorting
order = input("enter 'asc' for ascending (or) 'desc' for descending order :").strip().lower()
#sort and print based on user input
if order == 'asc':
    sorted_colors = sorted(colors)
    print("colors in ascending order:")
    print(sorted_colors)

elif order == 'desc':
    sorted_colors = sorted(colors,reverse=True)
    print("colors in descending order :")
    print(sorted_colors)
else:
    print("invalid input please enter 'asc or 'desc'.")
