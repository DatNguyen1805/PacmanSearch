# PacmanSearch
# 18020287-Nguyễn Tiến Đạt
## Câu 1: Tìm kiếm theo chiều sâu (DFS)

![DFS](https://user-images.githubusercontent.com/71663050/94950845-77598000-050d-11eb-8899-de5e7753d971.PNG)
- Tạo fringe theo kiểu Stack() chứa các node trong quá trình duyệt bài toán. Cho điểm xuất phát vào trong fringe
- Bắt đầu vòng lặp while: nếu fringe rỗng thì return luôn. Sau đó pop đỉnh đầu trong fringe ra vào gọi nó là node, cho vào visisted. Nếu nó là đích luôn thì tìm kiếm thành công, còn không thì duyệt tất cả các thành phần con của node không thuộc fringe và visited, push nó vào đầu fringe như trong code
- Vòng lặp kết thúc khi không còn đỉnh nào cần duyệt hoặc tìm được đích

## Câu 2: Tìm kiếm theo chiều rộng (BFS)

![BFS](https://user-images.githubusercontent.com/71663050/94951632-dbc90f00-050e-11eb-850e-927ebe32fb4a.PNG)
- Bài toán về cơ bản giống như bài DFS chỉ khác là ta sẽ tạo fringe theo kiểu Queue(), cho các nút vào hàng đợi chứ không phải ngăn xếp như câu 1
- Duyệt vòng lặp tương tự như câu 1

## Câu 3: Tìm kiếm theo chi phí thấp nhất (UCS)

![UCS](https://user-images.githubusercontent.com/71663050/94952159-ba1c5780-050f-11eb-8989-07db6e3da17b.PNG)
- Thay vì sử dụng Queue như câu 2 thì chúng ta sử dụng PriorityQueue() hay còn gọi là hàng đợi ưu tiên, node nào có mức độ ưu tiên cao hơn tương đương
với chi phí thấp hơn thì sẽ được duyệt trước
- Duyệt giống như các bài trên nhưng ở bước cuối của vòng lặp thì sẽ push vào fringe theo thứ tự tăng dần về khoảng cách từ đỉnh xuất phát đến đỉnh đang xét

## Câu 4: Thuật toán tìm kiếm A*

![A](https://user-images.githubusercontent.com/71663050/94954107-cc4bc500-0512-11eb-944d-d7af35fd4e08.PNG)
- Chúng ta vẫn sử dụng PriorityQueue() như bài UCS 
- Tương tự duyệt giống như UCS nhưng sẽ push vào fringe theo thứ tự tăng dần của f(X) với f(X) = g(X) + h(X) trong đó:
     g(X) là khoảng cách từ đỉnh xuất phát đến X (Công thức trong bài UCS), 
     h(X) là khoảng cách từ X đến đỉnh đích
     
## Câu 5: Tìm tất cả các góc (Finding all the corners)

![Q5](https://user-images.githubusercontent.com/71663050/94965468-c01d3300-0525-11eb-96bc-8a2eb011462f.PNG)
- Đầu tiên với hàm trả về trạng thái bắt đầu thì thì sẽ return startingPosition là vị trí bắt đầu, và các góc chưa được truy cập self.corners
- Với hàm isGoalState kiểm tra xem Pacman đã tới hết các góc chưa và trả về True/False
- Hàm getSuccessor kiểm tra các hướng, cập nhất trạng thái và trả về các successor có thế đi được

## Câu 6: Corners Problem: Heuristic

![Q6](https://user-images.githubusercontent.com/71663050/94967515-6a4a8a00-0529-11eb-87be-f5693dbe3907.PNG)
- Hàm cornerHeuristic sẽ tính khoảng cách từ vị trí hiện tại đến từng góc chưa tới và sẽ trả về khoảng cách tới góc xa nhất

## Câu 7:  Ăn hết dấu chấm

![Q7](https://user-images.githubusercontent.com/71663050/94969749-7cc6c280-052d-11eb-8757-7a3fbcd07b9a.PNG)
- Câu này ta sẽ sử dụng lại thuật toán BFS để giải quyết bài toán này. Chi tiết em sẽ mô tả ở trong video youtube

## Câu 8: Suboptimal Search
- Câu này cũng sử dụng BFS tìm kiếm với trạng thái kết thúc là tọa độ hạt thức ăn bất kì được đưa đến
