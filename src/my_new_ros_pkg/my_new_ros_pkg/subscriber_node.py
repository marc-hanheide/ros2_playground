import rclpy

from rclpy.node import Node
from std_msgs.msg import String

class MySubscriberNode(Node):
    def __init__(self):
        super().__init__('my_subscriber')
        self.get_logger().info('Hello, ROS2!')
        self.create_subscription(
            String,
            'foo',
            self.callback,
            10)
    def callback(self, msg):
        self.get_logger().info('I heard: [%s]' % msg.data)

def main():
    rclpy.init()
    node = MySubscriberNode()
    rclpy.spin(node)
    rclpy.shutdown()
