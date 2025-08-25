from pages.Drag_and_drop_page import DragAndDropPage

class TestDragAndDropPage:

    def setup_method(self):
        self.drag_and_drop_page = DragAndDropPage(self.driver)

    def test_open_from_nav_bar(self):
        self.drag_and_drop_page.open()
        self.drag_and_drop_page.open_current_page_from_nav(self.drag_and_drop_page.DRAG_AND_DROP_LINK_LOCATOR)
        assert self.drag_and_drop_page.driver.current_url == self.drag_and_drop_page.PAGE_URL, \
            "Wrong link in nav bar for 'Drag and Drop'"

    def test_drag_and_drop(self):
        self.drag_and_drop_page.open()
        self.drag_and_drop_page.drag_and_drop(self.drag_and_drop_page.DRAGGABLE_LOCATOR,
                                              self.drag_and_drop_page.DROPPABLE_LOCATOR)
        assert self.drag_and_drop_page.get_text(self.drag_and_drop_page.DROPPABLE_TEXT_LOCATOR) == "Dropped!", \
            "Error logic drag and drop (wrong result text)"

    def test_drag_and_drop_smile(self):
        self.drag_and_drop_page.open()
        self.drag_and_drop_page.go_to_smile()
        self.drag_and_drop_page.drag_and_drop(self.drag_and_drop_page.IMG_LOCATOR,
                                              self.drag_and_drop_page.DROPPABLE_2_LOCATOR)
        assert self.drag_and_drop_page.is_smile_text_visible(2)
        assert not self.drag_and_drop_page.is_smile_text_visible(1)
        self.drag_and_drop_page.drag_and_drop(self.drag_and_drop_page.IMG_LOCATOR,
                                              self.drag_and_drop_page.DROPPABLE_1_LOCATOR)
        assert self.drag_and_drop_page.is_smile_text_visible(1)
        assert not self.drag_and_drop_page.is_smile_text_visible(2)
        self.drag_and_drop_page.drag_and_drop(self.drag_and_drop_page.IMG_LOCATOR,
                                              self.drag_and_drop_page.DROPPABLE_2_LOCATOR)
        assert self.drag_and_drop_page.is_smile_text_visible(2)
        assert not self.drag_and_drop_page.is_smile_text_visible(1)

