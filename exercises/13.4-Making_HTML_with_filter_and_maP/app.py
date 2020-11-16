all_colors = [
	{"label": 'Red', "sexy": True},
	{"label": 'Pink', "sexy": False},
	{"label": 'Orange', "sexy": True},
	{"label": 'Brown', "sexy": False},
	{"label": 'Pink', "sexy": True},
	{"label": 'Violet', "sexy": True},
	{"label": 'Purple', "sexy": False},
]

#Your code go here:
def filter_colors(x):
    if x['sexy']==True:
        return x['label']

   
def generate_li(y):
    return f"<li>{y['label']}</li>"

result=list(map(generate_li,(list(filter(filter_colors,all_colors)))))
end=""
for x in result:    
    end+=x
print(end)