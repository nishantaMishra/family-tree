import json

# family data
data = {
    "name": "प्रपितामह",
    "children": [
        {
            "name": "बेनीमाधव मिश्रा",
            "children": [
                {"name": "राम कृपाल मिश्रा",
                "children": [
                    {"name": "सत्यपाल(अन्नू) मिश्रा",
                    "children": [
                        {"name": "कन्धैया"},
                        {"name": "२"}
                    ]
                    },
                    {"name": "कृष्णपाल(कमलेश) मिश्रा",
                    "children": [
                        {"name": "सोनू"}
                    ]
                    },
                    {"name": "बिन्दु(गुलाबकली) मिश्रा"},
                    {"name": "नानबुदी"},
                    {"name": "मीनू"}
            ]
                },
                {"name": "राम शिरोमणि मिश्रा",
                "children": [
                    {"name": "दयाशङ्कर मिश्रा",
                    "children": [
                        {"name": "उदय"},
                        {"name": "छोटकौ"}
                    ]
                    },
                    {"name": "उमाशङ्कर मिश्रा",
                    "children": [
                        {"name": "बबलू"},
                        {"name": "झल्लू"},
                        {"name": "फुन्नू"}
                    ]
                    },
                    {"name": "३"},
                    {"name": "४"},
                    {"name": "५"}
                ]
                },
                {"name": "रमजनिया"},
                {"name": "सुदामा प्रसाद मिश्रा",
                "children": [
                    {"name": "सुरोश मिश्रा",
                    "children": [
                        {"name": "प्रमोद (त्यागी)"},
                        {"name": "विनोद (कल्लू)"},
                        {"name": "आनन्द"}
                    ]},
                    {"name": "मुनेश",
                    "children": [
                        {"name": "विकास"},
                        {"name": "खुशबू"},
                        {"name": "सुभाष"}
                    ]},
                    {"name": "सुनीता"},
                    {"name": "गीता"},
                    {"name": "सीता", "details": "इनका निधन आत्मदाह से हुआ था।"},
                    {"name": "ममता"}
                ]},
                {"name": "राम सूरत मिश्रा",
                "children": [
                    {"name": "अनुराधा तिवारी",
                    "children": [
                        {"name": "अनुराग तिवारी"},
                        {"name": "अंशु तिवारी"}
                    ]},
                    {"name": "श्रवण कुमार मिश्रा",
                    "children": [
                        {"name": "चेतना"},
                        {"name": "भावना"},
                        {"name": "प्रेरणा","url": "https://www.instagram.com/mishraprerna269/"},
                        {"name": "निशान्त मिश्रा"}
                    ]},
                    {"name": "आशिष कुमार मिश्रा"}
                ]}
            ]
        },
        {
            "name": "राम आश्रय मिश्रा",
            "children": [
                {"name": "राम प्रसाद मिश्रा",
                "children": [
                    {"name": "अशोक प्रसाद (मुन्नू)"},
                    {"name": "मनोज"},
                    {"name": "प्रदीप (छोटकौ)"},
                    {"name": "गुड्डन्"},
                    {"name": "करुणा"},
                    {"name": "पुष्पा"},
                    {"name": "सुधा"}
                ]},
                {"name": "सावित्री"}
            ]
        },
        {
            "name": "नारायण दीन मिश्रा",
            "children": [
                {"name": "सतीश",
                "children": [
                    {"name": "नीलू"},
                    {"name": "रेखा"},
                    {"name": "गुड्डी"}
                ]},
                {"name": "केशव",
                "children": [
                    {"name": "रानी"},
                    {"name": "गुड्डू"},
                    {"name": "अज्जू"}
                ]},
                {"name": "दिवाकर",
                "children": [
                    {"name": "१"},
                    {"name": "२"},
                    {"name": "३"},
                    {"name": "४"},
                    {"name": "५"}
                ]}
            ]
        }
        
    ]
}

data_json = json.dumps(data)

###### HTML template #######
html_template = f"""
<!DOCTYPE html>
<html lang="hi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mishra Family Chart</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
        }}
        .node {{
            cursor: pointer;
        }}
        .node circle {{
            fill: #999;
            stroke: steelblue;
            stroke-width: 3px;
        }}
        .node text {{
            font: 12px sans-serif;
        }}
        .link {{
            fill: none;
            stroke: #555;
            stroke-opacity: 0.4;
            stroke-width: 1.5px;
        }}
        #bottombar {{
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background-color: #f4f4f4;
            border-top: 1px solid #ddd;
            padding: 20px;
            box-shadow: 0 -2px 5px rgba(0,0,0,0.1);
            overflow-y: auto;
            height: 200px;
        }}
    </style>
    <script src="https://d3js.org/d3.v5.min.js"></script>
</head>
<body>
    <div id="bottombar">
        <h2>इतिहास</h2>
        <div id="details">जानकारी देखने के लिए व्यक्ति के नाम के स्पर्श करें।</div>
    </div>
    <script>
        var data = {data_json};

        var margin = {{top: 20, right: 120, bottom: 220, left: 120}},  // Adjust bottom margin to make space for the bottom bar
            width = 960 - margin.right - margin.left,
            height = 800 - margin.top - margin.bottom;

        var i = 0,
            duration = 750,
            root;

        var tree = d3.tree().size([height, width]);

        var diagonal = d3.linkHorizontal().x(d => d.y).y(d => d.x);

        var svg = d3.select("body").append("svg")
            .attr("width", width + margin.right + margin.left)
            .attr("height", height + margin.top + margin.bottom)
          .append("g")
            .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

        root = d3.hierarchy(data, d => d.children);
        root.x0 = height / 2;
        root.y0 = 0;

        function collapse(d) {{
          if (d.children) {{
            d._children = d.children;
            d._children.forEach(collapse);
            d.children = null;
          }}
        }}

        root.children.forEach(collapse);
        update(root);

        function update(source) {{
          var treeData = tree(root);

          var nodes = treeData.descendants(),
              links = treeData.descendants().slice(1);

          nodes.forEach(d => {{ d.y = d.depth * 180; }});

          var node = svg.selectAll('g.node')
              .data(nodes, d => d.id || (d.id = ++i));

          var nodeEnter = node.enter().append('g')
              .attr('class', 'node')
              .attr('transform', d => 'translate(' + source.y0 + ',' + source.x0 + ')')
              .on('click', click);

          nodeEnter.append('circle')
              .attr('class', 'node')
              .attr('r', 1e-6)
              .style('fill', d => d._children ? 'lightsteelblue' : '#fff');

          nodeEnter.append('text')
              .attr('dy', '.35em')
              .attr('x', d => d._children ? -13 : 13)
              .attr('text-anchor', d => d._children ? 'end' : 'start')
              .text(d => d.data.name);

          var nodeUpdate = nodeEnter.merge(node);

          nodeUpdate.transition()
              .duration(duration)
              .attr('transform', d => 'translate(' + d.y + ',' + d.x + ')');

          nodeUpdate.select('circle.node')
              .attr('r', 10)
              .style('fill', d => d._children ? 'lightsteelblue' : '#fff')
              .attr('cursor', 'pointer');

          var nodeExit = node.exit().transition()
              .duration(duration)
              .attr('transform', d => 'translate(' + source.y + ',' + source.x + ')')
              .remove();

          nodeExit.select('circle')
              .attr('r', 1e-6);

          nodeExit.select('text')
              .style('fill-opacity', 1e-6);

          var link = svg.selectAll('path.link')
              .data(links, d => d.id);

          var linkEnter = link.enter().insert('path', 'g')
              .attr('class', 'link')
              .attr('d', d => {{
                var o = {{x: source.x0, y: source.y0}};
                return diagonal({{source: o, target: o}});
              }});

          var linkUpdate = linkEnter.merge(link);

          linkUpdate.transition()
              .duration(duration)
              .attr('d', d => diagonal({{source: d.parent, target: d}}));

          link.exit().transition()
              .duration(duration)
              .attr('d', d => {{
                var o = {{x: source.x, y: source.y}};
                return diagonal({{source: o, target: o}});
              }})
              .remove();

          nodes.forEach(d => {{
            d.x0 = d.x;
            d.y0 = d.y;
          }});

          function click(d) {{
            if (d.children) {{
              d._children = d.children;
              d.children = null;
            }} else {{
              d.children = d._children;
              d._children = null;
            }}
            update(d);
            showDetails(d.data);
          }}
        }}

        function showDetails(data) {{
            var detailsDiv = document.getElementById('details');
            detailsDiv.innerHTML = '<h3>' + data.name + '</h3><p>' + data.details + '</p>';
        }}
    </script>
</body>
</html>
"""


with open("index.html", "w") as file:
    file.write(html_template)

print("Family tree HTML file was created: index.html")

