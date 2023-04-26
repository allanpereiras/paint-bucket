class Painter:
    def __init__(self, image):
        """Initialize a new Painter object with an image matrix"""
        self.image = image
        self.current_carac = None
        self.new_carac = None

    def within_bounds(self, pixel):
        """Check if a pixel is within the bounds of the image matrix"""
        return (0 <= pixel[0] < len(self.image[0])) and (0 <= pixel[1] < len(self.image))

    def get_neighbors(self, pixel):
        """
        Get neighboring pixels of a given pixel that share the same carac
        and are within the bounds of the image matrix
        """
        x, y = pixel
        neighbors = []
        if x > 0 and self.image[y][x-1] == self.current_carac:
            neighbors.append((x-1, y))
        if y > 0 and self.image[y-1][x] == self.current_carac:
            neighbors.append((x, y-1))
        if x < len(self.image[0]) - 1 and self.image[y][x+1] == self.current_carac:
            neighbors.append((x+1, y))
        if y < len(self.image) - 1 and self.image[y+1][x] == self.current_carac:
            neighbors.append((x, y+1))
        return neighbors

    def paint_pixel(self, pixel):
        """Paint a pixel with the new carac"""
        self.image[pixel[1]][pixel[0]] = self.new_carac

    def paint_region(self, pixel):
        """
        Recursively paint the region that is connected to the starting pixel
        via its neighbors in the same row or column and share the same carac
        """
        if not self.within_bounds(pixel) or self.image[pixel[1]][pixel[0]] == self.new_carac:
            # Stop recursion if the pixel is out of bounds or already painted
            return
        if self.image[pixel[1]][pixel[0]] == self.current_carac:
            # Paint the pixel if it shares the same carac as the starting pixel
            self.paint_pixel(pixel)
            # Recursively paint neighboring pixels that share the same carac
            for neighbor in self.get_neighbors(pixel):
                self.paint_region(neighbor)

    def paint(self, start_pixel, new_carac):
        """
        Entry point for the paint operation, which sets the current and
        new caracs and calls the paint_region method to fill the region
        """
        self.current_carac = self.image[start_pixel[1]][start_pixel[0]]
        self.new_carac = new_carac
        if self.new_carac == self.current_carac:
            # Stop operation if the new carac is the same as the current carac
            return
        self.paint_region(start_pixel)