<template>
  <section id="models" class="models-section">
    <h2> Data Processing and Code</h2>
    
    <div class="model-section">
      <h3 class="model-title">1. Element-Level</h3>
      <div class="model-content">
        <div class="model-text">
          <p>
            We integrate several advanced deep learning models with a rule-based algorithm for slide structure extraction to analyze the slide objects obtained from preprocessing. 
            We use the TextBox[1] to detect text boxes in images and recognize text content.
          </p>
          
          <div class="code-container">
            <div class="code-block">
              <pre><code class="language-python"><span class="python-builtin">net</span> = <span class="python-module">caffe</span>.<span class="python-function">Net</span>(<span class="python-variable">config</span>[<span class="python-string">'model_def'</span>], <span class="python-variable">config</span>[<span class="python-string">'model_weights'</span>], <span class="python-module">caffe</span>.<span class="python-constant">TEST</span>)
<span class="python-variable">detections</span> = <span class="python-builtin">net</span>.<span class="python-function">forward</span>()[<span class="python-string">'detection_out'</span>]
<span class="python-variable">bboxes</span> = <span class="python-function">extract_detections</span>(<span class="python-variable">detections</span>, <span class="python-variable">config</span>[<span class="python-string">'det_score_threshold'</span>], <span class="python-variable">image_height</span>, <span class="python-variable">image_width</span>)
<span class="python-variable">results</span> = <span class="python-function">apply_quad_nms</span>(<span class="python-variable">bboxes</span>, <span class="python-variable">config</span>[<span class="python-string">'overlap_threshold'</span>])
<span class="python-function">save_and_visu</span>(<span class="python-variable">image</span>, <span class="python-variable">results</span>, <span class="python-variable">config</span>)</code></pre>
            </div>
          </div>
        </div>
      </div>
    </div>
    
    <div class="model-section">
      <h3 class="model-title">2. Event-Level</h3>
      <div class="model-content">
        <div class="model-text">
          <p>
            Based on element-level data, we categorized event-level data into attributes and relationships.
          </p>
          
          <h4>2.1. Extract The Delivery Style</h4>
          <p>
            We perform video segmentation by analyzing the extracted video text through word vectorization and incorporating handwritten text recognized by Tesseract[2].
          </p>
          
          <h4>2.2. Chain-of-Thought Prompt</h4>
          <p>
            Leveraging the Chain-of-Thought model proposed by Wei et al.[3], we employed GPT-3.5 to identify concept relationships.
          </p>
          
          <div class="code-block">
            <pre><code class="language-json">{
<span class="python-string">"Note that your response should only be in JSON format; there is no need to add any statements. I want you to play the role of a data analysis expert who is good at finding the connection between
[concept] and various concepts. Your reasoning process should be step-by-step, clearly displaying the results of each step. Your workflow should include the following:

1.Firstly, I will provide you with the teacher's explanation of the current concept in this course, please read the explanation carefully: [subtitle]

2.Currently, you have roughly learned about the relevant content of this concept. Please analyze the association of this concept with the following concepts: [concept list]

3.There are three levels of relationships between associated concepts: association, similarity, and inclusion. Please carefully identify which relationship the concept has with associated concepts, and finally provide feedback to me in JSON format.

4.The specific format is as follows:

[
		{
\"concept1\": \" \", 
\"concept2\": \"\",
\"relationship\": \"association/similarity/inclusion\",
}
]

Here, is the text I need you to process: \"...\"</span>"
}</code></pre>
          </div>
        </div>
      </div>
    </div>
    
    <div class="model-section">
      <h3 class="model-title">3. Conclusion Level</h3>
      <div class="model-content">
        <div class="model-text">
          <p>
            To capture important time nodes within the course, we integrated the duration and relationships extracted from the element-level data.
          </p>
          
          <h4>3.1. Element Data Format</h4>
          <p>
            By integrating the extracted content from three levels, we have defined the data structure for each Element as follows:
          </p>
        </div>
      </div>

      <div class="inline-code-image">
        <div class="code-side">
          <div class="code-block">
            <pre><code class="language-json">
{
  <span class="python-string">"id"</span>: <span class="python-string">"equation0"</span>,
  <span class="python-string">"boundingBox"</span>: {...},
  <span class="python-string">"timeDur"</span>: [...],
  <span class="python-string">"type"</span>: <span class="python-string">" "</span>,
  <span class="python-string">"isConcept"</span>: [...],
  <span class="python-string">"concepts"</span>: [...],
  <span class="python-string">"serveConcepts"</span>: [...],
  <span class="python-string">"conTime"</span>: [...]
}</code></pre>
          </div>
        </div>
        <div class="image-side">
          <img src="../assets/out_json.png" alt="JSON Output Example" />
        </div>
      </div>

      <div class="model-content">
        <div class="model-text">
          <h4>3.2. Important Time Node Data Format</h4>
          <p>
            We have defined the data structure for each important time node as follows:
          </p>
        </div>
      </div>

      <div class="inline-code-image">
        <div class="code-side">
          <div class="code-block">
            <pre><code class="language-json">
{
  <span class="python-string">"id"</span>: <span class="python-string">" "</span>,
  <span class="python-string">"layout"</span>: "",
  <span class="python-string">"name"</span>: "",
  <span class="python-string">"time"</span>: [...],
  <span class="python-string">"text"</span>: [...],
  <span class="python-string">"attribute"</span>: [...],
  <span class="python-string">"timeFatherId"</span>: "",
  <span class="python-string">"timeSonId"</span>: "",
  <span class="python-string">"basicRel"</span>: [...],
  <span class="python-string">"similarityRel"</span>: [...],
  <span class="python-string">"son"</span>: [...],
  <span class="python-string">"father"</span>: [...],
  <span class="python-string">"type"</span>: "",
  <span class="python-string">"totalDuration"</span>: ,
  <span class="python-string">"tags"</span>: [...],
  <span class="python-string">"serTags"</span>: [...],
}</code></pre>
          </div>
        </div>
        <div class="image-side2">
          <img src="../assets/frame_json.png" alt="JSON Output Example" />
        </div>
      </div>
    </div>

    <div class="model-section">
      <h3 class="model-title">References</h3>
      <div class="references-content">
        <div class="reference-item">
          <span class="reference-number">[1]</span>
          <p class="reference-text">
            Minghui Liao, Baoguang Shi, Xiang Bai, Xinggang Wang, Wenyu Liu. TextBoxes: A Fast Text Detector with a Single Deep Neural Network. AAAI 2017.
          </p>
        </div>

        <div class="reference-item">
          <span class="reference-number">[2]</span>
          <p class="reference-text">
            R. Smith, D. Antonova, and D.-S. Lee, “Adapting the tesseract open source ocr engine for multilingual ocr,” in Proceedings of the International Workshop on Multilingual OCR, 2009, pp. 1–8.
          </p>
        </div>

        <div class="reference-item">
          <span class="reference-number">[3]</span>
          <p class="reference-text">
            J. Wei, X. Wang, D. Schuurmans, M. Bosma, F. Xia, E. Chi, Q. V. Le, D. Zhou et al., “Chain-of-thought prompting elicits reasoning in large language models,” Advances in Neural Information Processing Systems, vol. 35, pp. 24 824–24 837, 2022.
          </p>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.models-section {
  max-width: 1200px;
  margin: 0 auto;
  padding: 40px 20px;
  color: #f8f8f8;
}

h2 {
  color: #ffffff;
  border-bottom: 2px solid #42b883;
  padding-bottom: 10px;
  margin-bottom: 40px;
  display: inline-block;
  font-size: 1.8em;
}

.model-section {
  margin-bottom: 60px;
  background-color: #2a2a2a;
  border-radius: 8px;
  padding: 30px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

.model-title {
  color: #42b883;
  font-size: 1.5em;
  margin-top: 0;
  margin-bottom: 20px;
  border-bottom: 1px solid #3a3a3a;
  padding-bottom: 10px;
}

.model-content {
  display: flex;
  flex-direction: column;
  gap: 30px;
}

.model-text {
  flex: 1;
}

.model-text p {
  color: #e0e0e0;
  line-height: 1.6;
  margin-bottom: 15px;
}

.model-text h4 {
  color: #42b883;
  margin-top: 25px;
  margin-bottom: 15px;
  font-size: 1.2em;
}

/* 全新的内联代码和图片容器 */
.inline-code-image {
  display: flex;
  flex-direction: row;
  gap: 20px;
  margin: 20px 0;
  align-items: flex-start;
}

.code-side {
  flex: 1;
  min-width: 0; /* 防止内容溢出 */
}

.image-side {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
}

.image-side img {
  max-width: 100%;
  max-height: 300px;
  border-radius: 4px;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.3);
}

.image-side2 {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
}

.image-side2 img {
  max-width: 100%;
  max-height: 400px;
  border-radius: 4px;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.3);
}

.code-container {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  margin: 20px 0;
}

.code-block {
  flex: 1;
  min-width: 300px;
  background-color: #1e1e1e;
  border-radius: 6px;
  padding: 15px;
  overflow-x: auto;
}

.code-block pre {
  margin: 0;
  color: #e0e0e0;
  font-family: 'Courier New', monospace;
  font-size: 14px;
  line-height: 1.5;
  text-align: left;
  white-space: pre-wrap;
  word-break: break-all;
}

.code-block code {
  font-family: 'Courier New', monospace;
}

/* Python 语法高亮 */
.python-keyword {
  color: #569cd6; /* 关键字 - 蓝色 */
}

.python-function {
  color: #dcdcaa; /* 函数 - 黄色 */
}

.python-module {
  color: #4ec9b0; /* 模块 - 青绿色 */
}

.python-builtin {
  color: #4ec9b0; /* 内置对象 - 青绿色 */
}

.python-string {
  color: #ce9178; /* 字符串 - 橙红色 */
}

.python-number {
  color: #b5cea8; /* 数字 - 浅绿色 */
}

.python-variable {
  color: #9cdcfe; /* 变量 - 浅蓝色 */
}

.python-constant {
  color: #569cd6; /* 常量 - 蓝色 */
}

.python-comment {
  color: #6a9955; /* 注释 - 绿色 */
}

strong {
  color: #42b883;
  font-weight: bold;
}

/* 响应式设计 */
@media (min-width: 768px) {
  .model-content {
    flex-direction: row;
  }
  
  .code-container {
    flex-direction: row;
  }
}

@media (max-width: 767px) {
  .model-content {
    flex-direction: column;
  }
  
  .code-container {
    flex-direction: column;
  }
  
  .code-block {
    min-width: auto;
  }
  
  /* 在小屏幕上转为垂直布局 */
  .inline-code-image {
    flex-direction: column;
  }
}

/* References 样式 */
.references-content {
  display: flex;
  flex-direction: column;
  gap: 20px;
  padding: 10px 0;
}

.reference-item {
  display: flex;
  gap: 15px;
  align-items: flex-start;
  color: #e0e0e0;
}

.reference-number {
  color: #42b883;
  font-weight: bold;
  min-width: 30px;
}

.reference-text {
  margin: 0;
  line-height: 1.6;
}

/* 响应式设计 */
@media (max-width: 767px) {
  .reference-item {
    flex-direction: column;
    gap: 5px;
  }
  
  .reference-number {
    min-width: auto;
  }
}
</style> 