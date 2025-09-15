<template>
  <section id="examples" class="section-container">
    <h2>Examples</h2>
    <div class="examples-content">
      <div class="video-section">
        <div class="video-container">
          <video controls>
            <source src="../assets/video.mp4" type="video/mp4">
            Your browser does not support the video tag.
          </video>
        </div>
        <div class="video-description">
          <h3>Demo Video</h3>
          <p>
            This video demonstrates how HyperMOOC augments educational content with
            interactive visualizations, showing the seamless integration of concepts
            and their relationships within the video timeline.For a clearer video version, please refer to:  <a href="https://www.youtube.com/watch?v=rdyb2Gj-sFM">https://www.youtube.com/watch?v=rdyb2Gj-sFM</a>
          </p>
        </div>
      </div>

      <div class="examples-grid">
        <div class="example-card">
          <div class="example-video">
            <video controls>
              <source src="../assets/demo1.mp4" type="video/mp4">
              Your browser does not support the video tag.
            </video>
          </div>
          <div class="example-description">
            <h3>Demo1: Play</h3>
            <p>At this stage, HyperMOOC achieves the learner’sunderstanding of the current concept by Highlighting the concepts in the video frames and subtitles</p>
          </div>
        </div>
        <div class="example-card">
          <div class="example-video">
            <video controls>
              <source src="../assets/demo2.mp4" type="video/mp4">
              Your browser does not support the video tag.
            </video>
          </div>
          <div class="example-description">
            <h3>Demo2: Focused</h3>
            <p>Given the limited prevalence and high complexity of eye-tracking devices, HyperMOOC currently implements Gaze interaction through mouse hover. </p>
          </div>
        </div>
        <div class="example-card">
          <div class="example-video">
            <video controls>
              <source src="../assets/demo3.mp4" type="video/mp4">
              Your browser does not support the video tag.
            </video>
          </div>
          <div class="example-description">
            <h3>Demo3: Paused</h3>
            <p>Learners Pause the video and switch to HyperMOOC’s full mode by clicking on elements within the video. </p>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.section-container {
  padding: 40px 0;
}

.examples-content {
  display: flex;
  flex-direction: column;
  gap: 40px;
}

.video-section {
  background: #fff;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  padding: 20px;
}

.video-container {
  width: 100%;
  max-width: 800px;
  margin: 0 auto;
  aspect-ratio: 16 / 9;
  background: #000;
  border-radius: 4px;
  overflow: hidden;
}

.video-container video {
  width: 100%;
  height: 100%;
  object-fit: contain;
}

.video-description {
  margin-top: 20px;
  padding: 0 20px;
  text-align: center;
}

.video-description h3 {
  color: #333;
  margin-bottom: 10px;
  font-size: 1.4em;
}

.video-description p {
  color: #666;
  line-height: 1.6;
  max-width: 600px;
  margin: 0 auto;
}

.examples-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
  margin-top: 30px;
}

.example-card {
  background: #fff;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease;
}

.example-card:hover {
  transform: translateY(-5px);
}

.example-card img {
  width: 100%;
  height: 200px;
  object-fit: cover;
}

.example-description {
  padding: 20px;
}

.example-description h3 {
  margin: 0 0 10px;
  color: #333;
}

.example-description p {
  margin: 0;
  color: #666;
  line-height: 1.5;
}

.example-video {
  width: 100%;
  aspect-ratio: 16/9;
  overflow: hidden;
  background: #000;
  display: flex;
  align-items: center;
  justify-content: center;
}

.example-video video {
  width: 100%;
  height: 100%;
  object-fit: contain;
}

@media (max-width: 1024px) {
  .examples-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 768px) {
  .examples-grid {
    grid-template-columns: 1fr;
  }
}
</style> 