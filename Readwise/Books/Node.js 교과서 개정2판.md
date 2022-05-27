# Node.js 교과서 개정2판

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/static/images/default-book-icon-8.18caceaece2b.png)

## Metadata
- Author: [[Cho Hyunyoung]]
- Full Title: Node.js 교과서 개정2판
- Category: #books

## Highlights
- Node.jsⓇ는 Chrome V8 Javascript 엔진으로 빌드된 Javascript 런타임
- 서버는 클라이언트의 요청에 대해 응답을 합니다.
- const express = require('express');
  const app = express();
  app.set('port', process.env.PORT || 3000);
  app.get('/', (req, res) => {
  res.send('Hello, Express');
  });
  app.listen(app.get('port'), () => {
  console.log(app.get('port'), '번 포트에서 대기 중');
  });
