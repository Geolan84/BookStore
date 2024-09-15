import 'package:book_client/domain/books_api_client.dart';
import 'package:elementary/elementary.dart';
import 'package:book_client/domain/book.dart';
import 'package:book_client/books_screen/books_screen.dart';

/// Model for [BooksScreen]
class BooksScreenModel extends ElementaryModel {
  final BooksApiClient apiClient;

  BooksScreenModel({required this.apiClient});

  Future<List<Book>> loadBooks() async {
    return apiClient.loadBooks();
  }
}
