<!DOCTYPE html>
<meta charset="utf-8">
<style>
    .node circle {
        fill: #999;
    }

    .node text {
        font: 10px sans-serif;
    }

    .link {
        fill: none;
        stroke: #555;
        stroke-width: 1.5px;
    }
</style>
<body>
<script src="https://d3js.org/d3.v6.min.js"></script>
<script>

function createDAG(people) {
    const width = 800;
    const height = 600;

    // Create a map of individuals
    const personMap = new Map();
    people.forEach(person => {
        personMap.set(person.name, {
            name: person.name,
            children: [],
            parents: []
        });
    });

    // Establish the relationships
    people.forEach(person => {
        const personNode = personMap.get(person.name);
        if (person.junior) {
            person.junior.split(',').forEach(juniorName => {
                const juniorNode = personMap.get(juniorName.trim());
                if (juniorNode) {
                    personNode.children.push(juniorNode);
                    juniorNode.parents.push(personNode);
                }
            });
        }
    });

    // Create an array of links for the DAG
    const links = [];
    personMap.forEach(node => {
        node.children.forEach(child => {
            links.push({ source: node, target: child });
        });
    });

    const simulation = d3.forceSimulation(Array.from(personMap.values()))
        .force("link", d3.forceLink(links).id(d => d.name).distance(100))
        .force("charge", d3.forceManyBody().strength(-300))
        .force("center", d3.forceCenter(width / 2, height / 2));

    const svg = d3.select("body").append("svg")
        .attr("width", width)
        .attr("height", height);

    const link = svg.selectAll(".link")
        .data(links)
        .enter().append("line")
        .attr("class", "link");

    const node = svg.selectAll(".node")
        .data(simulation.nodes())
        .enter().append("g")
        .attr("class", "node")
        .call(d3.drag()
            .on("start", dragstarted)
            .on("drag", dragged)
            .on("end", dragended));

    node.append("circle")
        .attr("r", 5);

    node.append("text")
        .attr("dy", 3)
        .attr("x", 8)
        .style("text-anchor", "start")
        .text(d => d.name);

    simulation.on("tick", () => {
        link
            .attr("x1", d => d.source.x)
            .attr("y1", d => d.source.y)
            .attr("x2", d => d.target.x)
            .attr("y2", d => d.target.y);

        node
            .attr("transform", d => `translate(${d.x},${d.y})`);
    });

    function dragstarted(event, d) {
        if (!event.active) simulation.alphaTarget(0.3).restart();
        d.fx = d.x;
        d.fy = d.y;
    }

    function dragged(event, d) {
        d.fx = event.x;
        d.fy = event.y;
    }

    function dragended(event, d) {
        if (!event.active) simulation.alphaTarget(0);
        d.fx = null;
        d.fy = null;
    }
}

const people = [
    { name: "Person A", senior: "", junior: "Junior A1, Junior A2" },
    { name: "Person B", senior: "", junior: "Junior A1, Junior B2, Junior B3" },
    { name: "Junior A1", senior: "Person A, Person B", junior: "" },
    { name: "Junior A2", senior: "Person A", junior: "" },
    { name: "Junior B2", senior: "Person B", junior: "" },
    { name: "Junior B3", senior: "Person B", junior: "" }
];

createDAG(people);

</script>
</body>
</html>
