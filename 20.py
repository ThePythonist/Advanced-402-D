header = input("Enter Header : " )
paragraph = input("Enter paragraph : " )

html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Testing HTML</title>
    <style>
        p {
          color: green;
          font-weight: bold;
        }

        h1 {
          color: red;
        }
    </style>
</head>
"""

html += """
<body>
<h1>{}</h1>
<p>{}</p>
</body>
</html>
""".format(header,paragraph)

open("index.html","w").write(html)
print("Done")
