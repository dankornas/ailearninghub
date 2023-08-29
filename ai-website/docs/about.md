---
hide:
    - path
    - navigation
    - footer
    - toc
---

<!DOCTYPE html>
<html>
<head>
<style>
.container {
  display: flex;
  justify-content: space-between;
}

.text {
  width: 45%;
  padding: 10px;
}

.image {
  width: 50%;
  padding: 20px;
  text-align: right;
}

.image img {
  border-radius: 10%;
  width: 100%;
  height: auto;
}

/* Change layout for smaller screens */
@media (max-width: 720px) {
  .container {
    flex-direction: column;
  }

  .text, .image {
    width: 100%;
    text-align: center;
  }
}
</style>
</head>
<body>

<div class="container">
  <div class="text">
    <h1> About Your Instructor </h1>
    <p>
        I'm a machine learning engineer, speaker, and AI educator on a mission to demystify the world of artificial intelligence and machine learning.
        <br></br>
        I have a passion for making complex concepts accessible to all and helping people from all walks of life understand and embrace the transformative power of AI and machine learning.
        <br></br>
        Whether you're a beginner or an experienced professional, my insights and expertise will help you stay ahead of the curve and take your skills to the next level. I'm excited to share my knowledge with you and help you on your journey to become an AI and machine learning expert!
    </p>
  </div>
  <div class="image">
    <img src="/ailearninghub/assets/images/me.jpg" alt="Your Image">
  </div>
</div>

</body>
</html>