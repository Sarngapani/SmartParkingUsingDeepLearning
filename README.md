# SmartParkingUsingDeepLearning
Abstract. Modern, efficient parking methods are therefore a must within the cities demanding modern infrastructural solutions. To illustrate this, the proposed solution, “Smart Parking using Deep Learning," employs technology of sophisticated object detection. We used YOLO V8, which incidentally is one of the most powerful algorithms out there and has a superb track record when it comes to the speed and efficiency of the detection of objects on images. In this system, we used the Python language, and there are several libraries of Python that are used in this system, as follows: CV2, OpenCV for video processing, Pandas for data operations, and NumPy for performing the numerical calculations. Our technique is an optimally placed camera capturing visuals in real time in a parking lot. Next are the YOLO V8 and OpenCV computation of these pictures and the CV2 to look for open parking spaces. While in the case of Pandas, the data is sorted logically so that space identification is efficient, here computation is fast. The proper structure of the proposed smart parking system should reduce the time used in search of adequate parking bays significantly. This assists in decreasing the flow of traffic in the parking lots. Due to flexibility, this system can be applied in various situations, such as an airport, a shopping mall, and so on. Thus, the idea of our project is that AI can be engaged in urban infrastructure to enhance people’s lives.
⦁	Introduction
⦁	Introduction to project
Thus, it is critical to monitor and manage parking on the background of the further growth and development in urban areas. To meet this need we have our project known as Smart Parking, this just enhances the Google maps for parking experience, the program uses object detection to find a parking space. This has prompted the research on improved algorithm and technology to decrease amazingly the time drivers use to look for a parking space. Therefore, the traffic circulation in all the city transport systems operating under Smart Parking will be optimised. 
 
The YOLO V8. 0 is integrated to support the system’s fundamental function as a Deep Learning Object Recognition Algorithm, the key upon which Smart Parking is based and one of the world’s fastest and most accurate. Such component as YOLO V8 makes the task of identifying available parking slots as fast as possible making this APK suitable for real time use. 
Our project integrates several powerful Python packages to deliver a seamless and efficient parking solution: 
cv2: Played a rather critical part while executing some tasks in image processing, cv2, which can be described as a component of OpenCV, can modify and study the incoming visual data. 
OpenCV: It is a moderate-level stage of computer vision and also a machine learning plan and it possesses several integral libraries which can be used for image processing. 
Pandas: A tool used rather effectively for data processing and harvesting that allowed to organize the received data regarding parking spaces as comprehensible. 
NumPy: A valuable suite of numbers, intended to enhance the calculation timeliness and powerfulness.
It is a Smart Parking system that uses an array of cameras to cover a car park in order to effectively monitor a parking lot space. These are live cameras that feed images of the parking area; they bring these images through YOLO V8 alongside OpenCV and cv2 to identify available parking spaces. Using Pandas, the data is transformed to form structures that would allow easy recognition of free spaces with ease and within a short span of time; in the same manner, NumPy has the capability of increasing the speed and efficiency of computations.  
The usage of our Smart Parking system should bring about a notable cut in time wasted searching for empty parking spaces, thus directly tackling one of the leading causes of traffic jams in parking lot facilities. This means that it can be used in a number of places such as airports, malls, and in the core urban areas hence its wide reach and interference. 
In general, our project demonstrates how artificial intelligence can be implemented in concrete structures of urban environment to optimize everyday life. Smarter parking is not just beneficial for the drivers, but for the cities and congested streets where they operate too since they help to eliminate traffic and provide solutions in calculating spaces and times well.
⦁	YOLOv8: 
YOLO (You Only Look Once) is another remarkable work in the real-time object detection method that made a shift in the field due to its lightning-processing speed and high accuracy of detection. Different from conventional solutions that involve reusing classifiers for detection, YOLO regards object detection as just a regression issue, and it returns the boxes and class probabilities simultaneously for full image inputs. It means that it is highly efficient for complicated processes that must be analysed immediately and in real time. 
Another key to the efficiency of the YOLO algorithm is the possibility of deep learning to detect several objects at one and the same time in an image. The fact that YOLO treats the entire object detection process as one single problem helps to eliminate the need for computational pipelines and reduce overlap in computation by large margins hence the improved performance. Because of its high, real-time image recognition ability, the computer vision technology is suitable for dynamics areas include auto-driving and video security. 
The current version is called YOLO V8, which updates the model and makes it even better to deal with due to the increased accuracy and less demand for computational power. YOLO V8 is constructed based on the enhancements of YOLO V7; it provides better localization and categorization of objects than previous versions while processing the data in real time. This blend of speed and quality cements YOLO V8 as a go-to solution for object recognition in real-time scenarios in multiple technological and industrial domains.           
 Fig. 1. Yolo-v8
⦁	Methodology
⦁	FLASK
Flask is an instance of a micro-Python web framework that aims at simplicity and easy flexibility for developing safe and free-of-charge web applications and web API.
⦁	CV2
cv2 is the library through which OpenCV functions are invoked in Python, and it includes numerous functions to operate in Computer Vision such as image processing, object identification, and video manipulation.
⦁	PICKLE
Pickle is a Python module, which is used for serializing and de-serializing an object of Python, which gives the functionality for storing data in a file and getting back the same as it is.
⦁	 ULTRALYTICS
Ultralytics offers advanced Artificial Intelligence and deep learning solutions ─ such as YOLOv5 ─ combined with tools to optimize the training and deployment of said models with ease.
⦁	CVZONE
CVZone is a Python library that simplifies computer vision tasks, integrating OpenCV with additional functionalities for image processing, object detection, and tracking, ideal for beginners.
⦁	YOLO V8
Perhaps one of the most famous object detection models of the present time is YOLOv8 – You Only Look Once version 8 that is famous for its high speed and accuracy. Therefore, similar to the previous versions, YOLOv8 employs deep convolutional neural network (CNN) and integrates the feature extraction and the bounding box prediction stages into a single stage. This approach allows some of the real-time object detection, which is very important for applications, where quick processing is important, for example self-driving cars or security cameras. YOLOv8 builds upon these principles by adding new architecture components, training schemes, and optimizations for enhancing the model’s accuracy in different object classes without compromising its speed. They also demonstrated a marked improvement relative to other methodologies typical of computer vision systems for their application in more solid and easy to scale solutions.
⦁	OpenCV
Open Source Computer Vision Library, often known as OpenCV, is a universal, open-source collection of programming interfaces for computer vision and image analysis. OpenCV was originally designed by Intel in 1999 and has since been adopted by a diverse community and supports various higher level programming languages including python, c++, Java etc. It can offer a set of functions and algorithms including image processing, object recognition, feature extraction and usage of a set of deep neural networks. People from various areas including robotics, healthcare, automotive and academic sectors use OpenCV for its efficiency, scalability and comprehensive documentations. Thanks to its further update and constant maintenance, CVLIB is needed for both academic and industry purpose of computer vision.
⦁	RTSP
RTSP (Real-Time Streaming Protocol) is a network control protocol which also used for use by the client in controlling the streaming media servers. It enables the important and unimpeded conveyance of physical audio and video information through IP networks. RU As clients, RTSP allows a form of control that is used to control the start and stop of streams among others, while servers allow for the handling of multiple stream requests at an instance. TCP or UDP base but most use port 554 in order to communicate. RTSP is adopted in environments in which real-time streaming is crucial, including surveillance systems, applications used in video conferences, and live streaming platforms. As a result, due to its capacity for negotiating transmission parameters, as well as managing session state, it can be considered as one of the basic protocols for interactive multimedia applications over the Internet.

              
Fig. 3. RTSP Protocol

⦁	Model Comparision
⦁	Significant Improvements in the model in comparison with existing models
⦁	 Advanced Object Detection Algorithm: 
⦁	The proposed model is built with YOLOv8 that is different from some of the previous models developed on YOLOv5 and below.  
⦁	YOLOV8 is the eighth version of the YOLO that is a family of object detection models by Ultralytics. YOLO models are rather fast and have high accuracy which makes them perfect for handling real-time object detection. YOLOv8 improves upon the previous versions leveraging the latest techniques to boost performance besides improving on the architectures.
⦁	 Inclusion of COCO Dataset: 
⦁	The strategy behind the creation of YOLOv8 and other models relies heavily on the COCO dataset known as Common Objects in Context.
⦁	The COCO dataset is used for fine-tuning of the YOLOv8 models, benchmarking and pretraining. The rich annotations, multiple categories, and, at the same time, simple but reasonable evaluation metrics make it a valuable informational base for the creation of models in computer vision. 
⦁	Due to the use of COCO, YOLOv8 is able to obtain very high accuracy and withstand disturbances in object detection tasks while leveraging on the serious research and development effort made on this database.

⦁	 Key Features and Improvements: 
⦁	 Architecture Enhancements:
⦁	 Improved Backbone and Neck: Improved backbone and neck implementation is part of YOLOv8 to enhance the extraction of features as well as the integration of compound scales in features. Thus, it results in better detection rate for objects of nearly all sizes that could be distinguished not by the limitation of the detecting ability but by the constraint of computational power. 
⦁	PANet Integration: Path Aggregation Network (PANet), is applied at the neck to optimize feature concatenation at the multi-scale enhancing object detection on small sized objects.
⦁	 Performance 
⦁	Speed and Efficiency: Also like the previous YOLO models, YOLOv8 is fast when making its predictions which makes it good for real-time use. 
⦁	Higher Accuracy: Due to enhanced architecture and the best practice in training procedures, the model of YOLOv8 is more accurate in detecting objects than the prior models. 
⦁	 Flexibility:  
⦁	Support for Multiple Tasks: The exhibits presented here are collected using YOLOv8, which is multifunctional and can be applied to necessities that incorporate object detection, instance segmentation, and multi-object tracking. 
⦁	Compatibility: It is intended to be extensible to different frameworks and can run on any stack from cloud servers down to the edge. 
⦁	System Architecture
The figure depicts the system architecture of the proposed smart parking system. It will be used to affect the automatic control of parking spaces in a parking lot. This is done using OpenCV—a rather popular open-source computer vision library—for capturing image data. It then analyzes the captured image to define parking space. To determine if a given parking space contains a vehicle or not, YOLOv8, an object detection model, is utilized. After the detection of these vehicles, the coordinates of each of them is used to check if the parking space is occupied or free. All this information is stored in the system. The system also incorporates a library known as Pickle to store the data. Real-time data stream (RTSP) is used in streaming real-time data over networks. The system can be employed in informing the users of the number of open spaces that are available in the lot. This information can be presented in a website. In general, the system is useful in enhancing efficiency about the management of parking lots due to its abilities in tracking the occupancy of parking spaces.
 
Fig. 4. System Architecture
⦁	


⦁	Implementation
⦁	 Defining Parking Slots
The polylines are used to outline the restricted areas and to draw parking slots which delimits the parking zone. Compared to the bounding boxes, polylines enable you to define certain numbers and shapes of parking slots on the video frame. This aids in making the system to know exactly where each parking space is situated.
 
Fig. 4. After Drawing Polylines
⦁	Check Occupancy
Once the parking slots are defined using polylines, the system can easily determine if there is a car within such region or not. Based on the positions of the cars as identified using the object detection algorithm with the polylines’ coordinates, the system can identify whether the parking slot is free or taken. Occupancy is monitored with the help of computer vision methodologies and deep learning.
 
Fig. 5. Checking for Parking Spaces

⦁	Display Slot Status
The smart parking system provides real-time display and monitoring of available parking spaces using real-time information provided by CCTV cameras. This data is processed and displayed on user interfaces allowing users to find available parking spaces efficiently.
    
Fig.6 . Slot Status Information

⦁	Result
The last of the smart parking system’s outputs is the web-based application that provides current information on the parking lot. The customers interact with the developed system using a web browser interface. Provides a clear output of the status of parking slots for easy identification by the customers. Attempts to denote the occupancy status of each of the identified parking areas using the two visible colors, red and green. Serves as an efficient means of informing the users within a brief instance about which of the slots are taken and which remain empty.  
total_slots: It gives the total number of parking slots that are to be provided.  
filled_slots: Number of slots currently filled by contenders and or placed under usage by the contender.  
empty_slots: Number of slots available at the given time when the analysis is being made.  
slot_status: A list of statuses of each parking stand where each stand can either be full (shown in red) or empty (shown in green).     
 
Fig.7  Slot Status Indication
⦁	Conclusion and further improvements
In conclusion, the developed smart parking project can be considered as useful as it adopts today’s advanced technologies to solve one of the real-world issues, which could be very helpful as a facilitator for controlling the distribution of parking places. It comes with strong operational capabilities and consumer interface; thus, it gives excellent potential for enhancing the motion and parking in the urban areas. 
⦁	Further Enhancements 
⦁	 Real-Time Updates :
There should be introduced the ways and means by which the current parking status can be changed with the need to refresh a page.  
⦁	 Notification System :
Messages or notifications need to be provided on the number of slots for the lot, a complete lot, a particular section available is full, etc.  
⦁	 Optimisation : 
To keep the variation of YOLO model at its minimum, Optimize the web server to increase the effectiveness and to pinpoint the efficiency.
⦁	 Security : 
The web interface together with their data storage and retrieval also requires basic level security for communication and access. 
These functionalities when incorporated in smart parking project offer an all-round solution when it comes to parking space control and management with computer vision and web technology to offer real time information to the users.
⦁	References
1.	Advanced Smart Parking Management System Development Using A; In Hwan Jung, Jae-Moon Lee and Kitae Hwang; School of Computer Engineering Hansung University,Korea; 2022.
2.	L. Zhang, J. Huang, X. Li and L. Xiong, "Vision-Based Parking-Slot Detection: A DCNN Based Approach and a Large-Scale Benchmark Dataset," in IEEE Transactions on Image Processing, vol. 27, no. 11, pp. 5350-5364, Nov. 2018.
3.	Chen, Lun-Chi, Ruey-Kai Sheu, Wen-Yi Peng, Jyh-Horng Wu, and Chien-Hao Tseng. 2020. "Video-Based Parking Occupancy Detection for Smart Control System" Applied Sciences 10, no. 3: 1079.
4.	Liu B, Lai H, Kan S, Chan C. Camera-Based Smart Parking System Using Perspective Transformation. Smart Cities. 2023; 6(2):1167-1184.	
