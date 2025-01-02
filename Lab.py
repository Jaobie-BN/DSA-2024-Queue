class Queue:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None
    
    def front(self):
        if not self.is_empty():
            return self.items[0]
        return None
    
    def size(self):
        return len(self.items)
    
    def display(self):
        print(f"Queue: {self.items}")

class Restaurant:
    def __init__(self):
        self.waiting_queue = Queue()
        
    def add_customer(self, name):
        self.waiting_queue.enqueue(name)
        print(f"ลูกค้า {name} เข้าคิวที่ {self.waiting_queue.size()}")
        
    def serve_customer(self):
        if not self.waiting_queue.is_empty():
            customer = self.waiting_queue.dequeue()
            print(f"กำลังเสิร์ฟลูกค้า: {customer}")
        else:
            print("ไม่มีลูกค้าในคิว")
            
    def show_queue(self):
        print(f"คิวปัจจุบัน: {self.waiting_queue.items}")
        print(f"จำนวนลูกค้าในคิว: {self.waiting_queue.size()}")
class BankQueue:
    def __init__(self):
        self.queue = Queue()

    def add_customer(self, customer_name, transaction_type):
        self.queue.enqueue((customer_name, transaction_type))

    def serve_customer(self):
        if self.queue.is_empty():
            print("ไม่มีลูกค้าในคิว")
        else:
            customer, transaction = self.queue.dequeue()
            print(f"ให้บริการ {customer} สำหรับ {transaction}")

    def show_queue(self):
        if self.queue.is_empty():
            print("ไม่มีลูกค้าในคิว")
        else:
            print("คิวปัจจุบัน:")
            for i, (customer, transaction) in enumerate(self.queue.items, start=1):
                print(f"{i}. {customer} - {transaction}")

    def estimated_wait_time(self):
        wait_time = self.queue.size() * 5
        print(f"เวลารอประมาณ: {wait_time} นาที")

# BarberQueue simulation
class BarberQueue:
    def __init__(self):
        self.queue = Queue()

    def add_customer(self, customer_name, service):
        self.queue.enqueue((customer_name, service))
        print(f"เพิ่มลูกค้า: {customer_name} ({service})")

    def show_queue(self):
        if self.queue.is_empty():
            print("ไม่มีลูกค้าในคิว")
        else:
            print("แสดงคิว:")
            total_time = 0
            for i, (customer, service) in enumerate(self.queue.items, start=1):
                service_time = self.get_service_time(service)
                total_time += service_time
                print(f"{i}. {customer} - {service} (รอประมาณ {total_time} นาที)")

    def call_next(self):
        if self.queue.is_empty():
            print("ไม่มีลูกค้าในคิว")
        else:
            customer, service = self.queue.dequeue()
            print(f"เรียกลูกค้า: {customer}")

    @staticmethod
    def get_service_time(service):
        times = {
            "ตัดผม": 30,
            "สระ": 20,
            "ย้อมสี": 60
        }
        return times.get(service, 0)

# Example simulation of BarberQueue
def main_barber():
    print("=== ร้านตัดผมคุณหรีด ===")
    barber = BarberQueue()
    barber.add_customer("สมชาย", "ตัดผม")
    barber.add_customer("สมหญิง", "ย้อมสี")
    barber.show_queue()
    barber.call_next()
    barber.show_queue()

main_barber()
