students = [
    {"name": "farbod", "job": "backend-dev", "code": "1101"},
    {"name": "parsa", "job": "front-dev", "code": "1102"},
    {"name": "amirali", "job": "database-admin", "code": "1103"},
    {"name": "amirali", "job": "project-manager", "code": "1104"},
    {"name": "shayan", "job": "software-analyst", "code": "1105"},
    {"name": "parham", "job": "backend-dev", "code": "1106"},
]

html = """
<!DOCTYPE html>
<html>
<head>
<style>
#customers {
  font-family: Arial, Helvetica, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

#customers td, #customers th {
  border: 1px solid #ddd;
  padding: 8px;
}

#customers tr:nth-child(even){background-color: #f2f2f2;}

#customers tr:hover {background-color: #ddd;}

#customers th {
  padding-top: 12px;
  padding-bottom: 12px;
  text-align: left;
  background-color: blue;
  color: white;
}
</style>
</head>
<body>

<h1>Developers</h1>

<table id="customers">
  <tr>
    <th>Name</th>
    <th>Job Ttile</th>
    <th>Code</th>
  </tr>
"""

for st in students:
    html += f"""
  <tr>
    <td>{st['name']}</td>
    <td>{st['job']}</td>
    <td>{st['code']}</td>
  </tr>
    """

html += """
</table>
</body>
</html>
"""

open("table.html", "w").write(html)
print("Done")
