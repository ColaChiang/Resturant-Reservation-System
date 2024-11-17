class ReservationSystem:
    def __init__(self):
        # 使用字典直接以電話號碼作為鍵，顧客名稱作為值
        self.reservations = {}

    def add_reservation(self, phone_number, name):
        # 直接以電話號碼作為鍵來存儲資料，避免雜湊衝突
        if phone_number in self.reservations:
            return f"警告：該電話號碼 {phone_number} 已有訂位，顧客為 {self.reservations[phone_number]}。"
        else:
            self.reservations[phone_number] = name
            return f"成功新增訂位：{name} 的電話號碼為 {phone_number}。"

    def linear_search_reservation(self, name):
        # 線性搜尋顧客名稱
        results = [
            f"找到訂位：顧客 {customer_name} 電話號碼 {phone}"
            for phone, customer_name in self.reservations.items() if customer_name == name
        ]
        if results:
            return "\n".join(results)
        return "找不到該顧客的訂位。"

    def quick_sort(self, reservations_list):
        # 快速排序實現
        if len(reservations_list) <= 1:
            return reservations_list
        pivot = reservations_list[0]  # 選取第一個元素作為樞軸
        less = [item for item in reservations_list[1:] if item[0] <= pivot[0]]
        greater = [item for item in reservations_list[1:] if item[0] > pivot[0]]
        return self.quick_sort(less) + [pivot] + self.quick_sort(greater)

    def list_reservations(self):
        # 使用快速排序對電話號碼排序
        reservations_list = list(self.reservations.items())
        sorted_reservations = self.quick_sort(reservations_list)
        return [
            {"phone_number": phone, "name": name}
            for phone, name in sorted_reservations
        ]

    def binary_search_reservation(self, phone_number):
        # 二分搜尋電話號碼
        sorted_reservations = self.quick_sort(list(self.reservations.items()))  # 使用快速排序
        low, high = 0, len(sorted_reservations) - 1
        while low <= high:
            mid = (low + high) // 2
            current_phone = sorted_reservations[mid][0]
            if current_phone == phone_number:
                return f"找到訂位：顧客 {sorted_reservations[mid][1]} 電話號碼 {phone_number}"
            elif current_phone < phone_number:
                low = mid + 1
            else:
                high = mid - 1
        return "找不到符合的電話號碼訂位。"
