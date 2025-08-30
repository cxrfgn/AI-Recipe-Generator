// 1. 等待DOM加载完成。
document.addEventListener('DOMContentLoaded', function() {
    // 2. 获取表单元素并为其添加'submit'事件监听器。
    const form = document.getElementById('preference-form');
    form.addEventListener('submit', function(event) {
        // 3. 阻止表单的默认提交行为。
        event.preventDefault();
        // 4. 收集表单中的数据。
        const forbidden = document.getElementById('forbidden').value.trim();
        const taste = document.getElementById('taste').value;
        const goal = form.querySelector('input[name="goal"]:checked').value;
        // 5. 组装成对象。
        const userPreferences = {
            forbidden,
            taste,
            goal
        };
        // 6. 打印到控制台。
        console.log(userPreferences);

        // 7. 模拟向后端发送请求。使用setTimeout模拟网络延迟。
        const resultsDiv = document.getElementById('recipe-results');
        resultsDiv.textContent = '正在为您生成食谱，请稍候...';
        try {
            setTimeout(() => {
                // 8. 2秒后，模拟接收到一个成功的响应
                // 修改模拟数据为数组形式
                const recipe = {
                    name: '健康鸡胸肉沙拉',
                    ingredients: ['鸡胸肉', '莴苣', '番茄', '橄榄油', '黑胡椒'],
                    steps: ['鸡胸肉煮熟切片', '莴苣和番茄洗净切块', '混合所有食材，加入橄榄油和黑胡椒拌匀'],
                    cuisine: '西式',
                    dietary_tags: '高蛋白、低脂肪'
                };
                // 9. 调用 displayRecipe 函数
                displayRecipe(recipe);
            }, 2000);
        } catch (error) {
            // 10. 模拟请求失败，显示错误提示
            resultsDiv.textContent = '食谱生成失败，请稍后重试。';
        }
    });

    // 显示食谱结果的函数
    function displayRecipe(recipe) {
        const resultsDiv = document.getElementById('recipe-results');
        // 清理先前结果
        resultsDiv.innerHTML = '';

        // 错误处理
        if (!recipe || !recipe.name) {
            resultsDiv.textContent = '未获取到食谱数据，请重试。';
            return;
        }

        // 标题
        const title = document.createElement('h2');
        title.textContent = `推荐食谱：${recipe.name}`;
        resultsDiv.appendChild(title);

        // 食材列表
        const ingTitle = document.createElement('p');
        ingTitle.innerHTML = '<strong>食材：</strong>';
        resultsDiv.appendChild(ingTitle);
        const ingList = document.createElement('ul');
        (Array.isArray(recipe.ingredients) ? recipe.ingredients : []).forEach(item => {
            const li = document.createElement('li');
            li.textContent = item;
            ingList.appendChild(li);
        });
        resultsDiv.appendChild(ingList);

        // 步骤列表
        const stepTitle = document.createElement('p');
        stepTitle.innerHTML = '<strong>步骤：</strong>';
        resultsDiv.appendChild(stepTitle);
        const stepList = document.createElement('ol');
        (Array.isArray(recipe.steps) ? recipe.steps : []).forEach(step => {
            const li = document.createElement('li');
            li.textContent = step.endsWith('。') ? step : step + '。';
            stepList.appendChild(li);
        });
        resultsDiv.appendChild(stepList);

        // 菜系
        const cuisine = document.createElement('p');
        cuisine.innerHTML = `<strong>菜系：</strong> ${recipe.cuisine || ''}`;
        resultsDiv.appendChild(cuisine);

        // 标签
        const tags = document.createElement('p');
        tags.innerHTML = `<strong>标签：</strong> ${recipe.dietary_tags || ''}`;
        resultsDiv.appendChild(tags);
    }
});
