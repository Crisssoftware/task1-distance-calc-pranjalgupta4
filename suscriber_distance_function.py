import rclpy
from rclpy.node import Node

import math

from turtlesim.msg import Pose
from std_msgs.msg import Float32


class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_suscriber')

        self.subscription = self.create_subscription(
            Pose, '/turtle1/pose', self.distance_callback, 10)
        self.subscription

        self.publisher_ = self.create_publisher(
            Float32, '/turtle1/distance_from_origin', 10)
        

    def distance_callback(self, msg):
        self.distance = math.sqrt(msg.x**2 + msg.y**2)
        self.get_logger().info('heloo!!')

        distance_msg = Float32()
        distance_msg.data = self.distance
        self.publisher_.publish(distance_msg)

        self.get_logger().info(f'Distance from origin: {self.distance:.2f}')


def main(args=None):
    rclpy.init(args=args)
    minimal_subscriber = MinimalSubscriber()
    rclpy.spin(minimal_subscriber)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
