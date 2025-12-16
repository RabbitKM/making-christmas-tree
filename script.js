document.getElementById('drawButton').addEventListener('click', drawTree);

function drawTree() {
    const height = parseInt(document.getElementById('height').value);
    const shape = document.getElementById('shape').value;
    const color = document.getElementById('color').value;
    const decorations = Array.from(document.querySelectorAll('.decorations input:checked')).map(cb => cb.value);

    let treeOutput = '';

    // 顏色映射 (簡單的 CSS 顏色)
    const colorMap = {
        'green': 'green',
        'blue': 'blue',
        'red': 'red'
    };
    const treeColor = colorMap[color] || 'green';

    // 根據形狀繪製樹
    if (shape === 'triangle') {
        for (let i = 1; i <= height; i++) {
            const spaces = ' '.repeat(height - i);
            const leaves = '*'.repeat(2 * i - 1);
            treeOutput += spaces + `<span style="color: ${treeColor};">${leaves}</span>\n`;
        }
    } else if (shape === 'star') {
        for (let i = 1; i <= height; i++) {
            if (i === 1) {
                treeOutput += ' '.repeat(height - 1) + `<span style="color: ${treeColor};">*</span>\n`;
            } else {
                const spaces = ' '.repeat(height - i);
                const leaves = '*'.repeat(2 * i - 1);
                treeOutput += spaces + `<span style="color: ${treeColor};">${leaves}</span>\n`;
            }
        }
    } else if (shape === 'pine') {
        for (let i = 1; i <= height; i++) {
            const spaces = ' '.repeat(height - i);
            const leaves = '*'.repeat(2 * i - 1);
            treeOutput += spaces + `<span style="color: ${treeColor};">${leaves}</span>\n`;
        }
    }

    // 樹幹
    const trunkWidth = Math.max(1, Math.floor(height / 5));
    const trunkHeight = Math.max(1, Math.floor(height / 4));
    for (let i = 0; i < trunkHeight; i++) {
        const spaces = ' '.repeat(height - Math.floor(trunkWidth / 2) - 1);
        const trunk = '|'.repeat(trunkWidth);
        treeOutput += spaces + `<span style="color: brown;">${trunk}</span>\n`;
    }

    // 添加裝飾
    if (decorations.includes('star')) {
        // 在樹頂添加星星
        treeOutput = ' '.repeat(height - 1) + '<span style="color: yellow;">*</span>\n' + treeOutput;
    }

    // 對於燈泡和裝飾球，我們需要修改現有的樹行
    let lines = treeOutput.split('\n');
    if (decorations.includes('lights') || decorations.includes('ornaments')) {
        for (let i = 0; i < lines.length - trunkHeight; i++) {  // 不修改樹幹
            if (lines[i].trim()) {
                let line = lines[i];
                if (decorations.includes('lights') && Math.random() < 0.3) {
                    // 隨機添加燈泡
                    const lights = ['<span style="color: red;">.</span>', '<span style="color: yellow;">.</span>', '<span style="color: blue;">.</span>', '<span style="color: green;">.</span>'];
                    const pos = Math.floor(Math.random() * line.length);
                    line = line.slice(0, pos) + lights[Math.floor(Math.random() * lights.length)] + line.slice(pos);
                }
                if (decorations.includes('ornaments') && Math.random() < 0.4) {
                    // 隨機添加裝飾球
                    const pos = Math.floor(Math.random() * line.length);
                    line = line.slice(0, pos) + '<span style="color: magenta;">O</span>' + line.slice(pos);
                }
                lines[i] = line;
            }
        }
        treeOutput = lines.join('\n');
    }

    document.getElementById('treeOutput').innerHTML = treeOutput;
}