from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        assert isinstance(strs, list), 'É necessário passar uma lista de palavras'
        assert all(isinstance(word, str) for word in strs), 'A lista deve conter somente strings'

        if self._validate_list_and_items(strs):
          raise ValueError('Verifique se a lista de palavras apresenta e cada palavra está entre 1 e 200!')

        common_prefix, *remaining_strs = strs

        for index in range(0, len(remaining_strs)):
          while True:
            if remaining_strs[index].startswith(common_prefix):
              break

            common_prefix = common_prefix[:len(common_prefix) - 1]

        return common_prefix

    @staticmethod
    def _validate_list_and_items(strs: List[str]) -> bool:
      list_length = len(strs)
      word_length_invalid = False

      if list_length == 0 or list_length > 200:
        return True

      for word in strs:
        word_length = len(word)

        if word_length == 0 or word_length > 200:
          word_length_invalid = True
          break

      return word_length_invalid