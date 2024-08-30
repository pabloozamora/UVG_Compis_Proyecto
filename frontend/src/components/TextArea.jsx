import React from "react";
import PropTypes from "prop-types";

function TextArea({ value, onChange }) {
  return (
    <textarea
      placeholder="Empieza a escribir CompiScript..."
      value={value}
      onChange={onChange}
      style={{ width: "100%", height: "200px" }}
    />
  );
}

TextArea.propTypes = {
    value: PropTypes.string.isRequired,
    onChange: PropTypes.func.isRequired,
};


export default TextArea;